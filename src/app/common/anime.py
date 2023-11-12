# coding:utf-8
import requests
import time
import re

from PyQt5.QtCore import QObject, pyqtSignal

from .utils import (
    Constants,
    remove_non_alphanum,
    compare_magnet_links,
    get_nyaa_search_result,
    get_time_diffrence,
    check_network
)


class Anime(QObject):
    """Class for managing the download of anime episodes or seasons."""
    infoSignal = pyqtSignal(str)
    errorSignal = pyqtSignal(str)
    successSignal = pyqtSignal(str)
    torrentSignal = pyqtSignal(list)

    def __init__(self, **kwargs):
        """Initialize an instance of the Anime class."""

        super().__init__()

        self.id = kwargs.get('id', 0)
        self.name = kwargs.get('name', '')
        self.search_name = kwargs.get('search_name', '')
        self.airing = kwargs.get('airing', False)
        self.next_eta = kwargs.get('next_eta', 0)
        self.total_episodes = kwargs.get('total_episodes', 1)
        self.last_aired_episode = (
            kwargs.get('last_aired_episode') if self.airing else self.total_episodes
        )
        self.season = kwargs.get('season', 1)
        self.format = kwargs.get('format', '')
        self.output_dir = kwargs.get('output_dir', '')
        self.img = kwargs.get('img', '')
        self.watch_url = kwargs.get('watch_url', '')
        self.episodes_to_download = kwargs.get('episodes_to_download', [])
        self.episodes_downloading = kwargs.get('episodes_downloading', [])
        self.episodes_downloaded = kwargs.get('episodes_downloaded', [])
        self.batch_download = kwargs.get('batch_download', True)
        self.watch_url = kwargs.get('watch_url', '')
        self.result = None

    def start(self):
        """Start downloading episodes or the entire season."""
        print(f'Looking into {self.name}')
        if self.episodes_downloading:
            self.check_downloading()

        if self.airing:
            self.check_currently_airing()

        if self.episodes_to_download:
            if self.batch_download:
                self.download_full()
            else:
                self.download_episodes()

        if (self.episodes_downloaded and
            not self.episodes_to_download and
            not self.episodes_downloading):
            print(f'Downloaded {self.name} completely.')
        elif self.airing and self.episodes_downloaded:
            downloaded_episodes = len(self.episodes_downloaded)
            print(f'Downloaded {self.name} till episode {downloaded_episodes}.')

    def download_full(self):
        """Download the full batch at once."""
        self.infoSignal.emit(f'Looking for {self.name}...')

        if self.airing:
            self.infoSignal.emit(f'{self.name} is still airing...')
            return False

        self.infoSignal.emit('searching')
        torrents = self.get_torrent_list()
        self.errorSignal.emit('searching')

        if not torrents:
            self.errorSignal.emit('No torrent found!')
            return False
        magnet = self.select_torrent(torrents)

        if not magnet:
            self.torrentSignal.emit([self.id, torrents])
            return False

        self.download_from_magnet(magnet, self.name)
        self.episodes_to_download = []
        self.episodes_downloading.append(('full', magnet))
        return True

    def download_episodes(self):
        """Download episodes one by one."""
        not_failed = True
        while (
            not_failed
            and self.episodes_to_download[0] <= self.last_aired_episode
        ):
            not_failed = self.download_episode(self.episodes_to_download[0])

    def download_episode(self, episode_number):
        """Download a single episode."""
        name = f'{self.name} S{self.season:02d}E{episode_number:02d}'
        self.infoSignal.emit(f'Looking for {name}')

        self.infoSignal.emit('searching')
        torrents = (
            self.result if self.result else self.get_torrent_list()
        )
        self.result = torrents
        self.errorSignal.emit('searching')

        if not torrents:
            self.errorSignal.emit(f'No torrent found for {name}')
            return False

        magnet = self.select_torrent(torrents, episode_number)

        if not magnet:
            self.errorSignal.emit('Torrent not found from preferred uploaders!')
            return False

        self.download_from_magnet(magnet, name)
        self.episodes_downloading.append((episode_number, magnet))

        episode_index = self.episodes_to_download.index(episode_number)
        del self.episodes_to_download[episode_index]

        if episode_number == self.total_episodes:
            return False

        return True

    def download_from_magnet(self, magnet_link, name):
        """Download a file using a magnet link.

        Args:
            magnet_link (str): The magnet link to use for the download.
            name (str): The name of the file being downloaded.
        """
        download_data = {'urls': magnet_link, 'savepath': self.output_dir}
        requests.post(
            f'{Constants.qbit_url}/api/v2/torrents/add', data=download_data
        )
        self.successSignal.emit(f'Download started {name}')

    def get_torrent_list(self):
        """Get a list of torrents for the given name.

        Returns:
            list: A list of tuples containing the title, magnet link, and size of torrents.
        """
        torrents = get_nyaa_search_result(self.search_name)

        if not torrents:
            self.errorSignal.emit('No result found...')
            self.infoSignal.emit('Trying Again...')

            if not check_network():
                self.errorSignal.emit('Internet connection not available!')
                exit()

            torrents = get_nyaa_search_result(self.search_name)

            if not torrents:
                self.errorSignal.emit(
                    'Either the anime is not available or the name is wrong!'
                )

        return torrents

    def select_torrent(self, torrents, episode_number="batch"):
        """Select the best torrent from a list of torrents.

        Args:
            torrents (list): A list of tuples containing the title, magnet link, and size of each torrent.
                The list should be already sorted by seeds.
            episode_number (int): The episode number to download. Default is batch which means download the full batch.

        Returns:
            str: The magnet link of the selected torrent.
        """
        name = re.escape(self.name)
        search_name = re.escape(self.search_name)
        season = f'(season {self.season})' if self.format != 'movie' else ''

        pattern = rf'\b({name}|{search_name})\b.*?\b1080p\b'
        regex = re.compile(pattern, re.IGNORECASE)

        if isinstance(episode_number, int):
            for title, magnet_link, size in torrents:
                if regex.search(title):
                    title_lower = title.lower()
                    if '[ember]' in title_lower:
                        additional = f' s{self.season:02}e{episode_number:02} '
                        if additional in title_lower:
                            return magnet_link
                    elif '[subsplease]' in title_lower:
                        additional = f'{" s " + str(self.season) if self.season >= 2 else ""} - {episode_number:02} '
                        if additional in title_lower:
                            return magnet_link
                    elif '[erai-raws]' in title_lower:
                        additional = f'{episode_number:02} '
                        if additional in title_lower:
                            return magnet_link
        else:
            for title, magnet_link, size in torrents:
                if regex.search(title):
                    title_lower = title.lower()
                    if any(keyword in title_lower for keyword in ['[ember]', '[judas]', '[subsplease]']):
                        if any(keyword in title_lower for keyword in ['batch', 'complete']):
                            if season in title_lower:
                                return magnet_link


        return ''

    def receive_data(self, data):
        """Receive data from an external source.

        Args:
            data (list): A list containing the name and magnet link of a file to download.
        """
        if not data:
            return
        name, magnet, size = data
        self.download_from_magnet(magnet, name)
        self.episodes_to_download = []
        self.episodes_downloading.append(('full', magnet))

    def check_downloading(self):
        """Check the status of any episodes that are currently being downloaded."""
        torrents = requests.get(f'{Constants.qbit_url}/api/v2/torrents/info').json()

        if self.episodes_downloading:
            for episode_number, magnet_link in self.episodes_downloading[:]:
                magnet_torrent = next(
                    (
                        torrent
                        for torrent in torrents
                        if compare_magnet_links(
                            torrent['magnet_uri'], magnet_link
                        )
                    ),
                    None,
                )
                torrent_name = magnet_torrent['name']

                if magnet_torrent and (magnet_torrent['progress'] * 100) == 100:
                    self.episodes_downloading.remove(
                        [episode_number, magnet_link]
                    )
                    self.episodes_downloaded.append(episode_number)
                    print(f'{torrent_name} has finished downloading :)')
                    requests.post(
                        f'{Constants.qbit_url}/api/v2/torrents/pause',
                        data={'hashes': magnet_torrent['hash']},
                    )
                else:
                    print(
                        f"{torrent_name} is {(magnet_torrent['progress'] * 100):.2f}% done & has {(magnet_torrent['eta']/60):.2f} mins left !!"
                    )

    def check_currently_airing(self):
        """Check if the anime is still airing and update the next_eta, last_aired_episode, and total_episodes attributes accordingly."""
        current_time = int(time.time())

        if self.next_eta > current_time:
            days, hours, minutes = get_time_diffrence(self.next_eta)
            print(
                f'Next episode airing in about {days} days {hours} hrs {minutes} mins'
            )
            return

        query = Constants.airing_query
        variables = {'id': self.id}
        url = Constants.api_url
        response = requests.post(url, json={'query': query, 'variables': variables})
        data = response.json()

        if data['data']['Media']['nextAiringEpisode'] is None:
            print(f'{self.name} has finished airing!')
            self.infoSignal.emit(f'{self.name} has finished airing!')
            self.last_aired_episode = self.total_episodes
            self.airing = False
            self.next_eta = 0
        else:
            self.next_eta = data['data']['Media']['nextAiringEpisode']['airingAt']
            self.last_aired_episode = (
                data['data']['Media']['nextAiringEpisode']['episode'] - 1
            )
            print(f'{self.name} episode {self.last_aired_episode} is airing')

    def to_dict(self):
        """Convert the Anime instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Anime instance.
        """
        return {
            'id': self.id,
            'name': self.name,
            'search_name': self.search_name,
            'season': self.season,
            'airing': self.airing,
            'batch_download': self.batch_download,
            'next_eta': self.next_eta,
            'format': self.format,
            'last_aired_episode': self.last_aired_episode,
            'total_episodes': self.total_episodes,
            'output_dir': self.output_dir,
            'watch_url': self.watch_url,
            'img': self.img,
            'episodes_to_download': self.episodes_to_download,
            'episodes_downloading': self.episodes_downloading,
            'episodes_downloaded': self.episodes_downloaded
        }

    @classmethod
    def from_dict(cls, data):
        """Create an Anime instance from a dictionary.

        Args:
            data (dict): A dictionary containing the data for the Anime instance.

        Returns:
            Anime: An Anime instance initialized with the given data.
        """
        return cls(**data)
