
from os import system
import sys
from signal import signal, SIGINT, SIGTERM
from re import findall
from pathlib import Path

import questionary

from prompt_toolkit.styles import Style
custom_style_fancy = Style([
    ('question', 'bold'),               # question text
    ('answer', 'fg:#f44336 bold'),      # submitted answer text behind the question
    ('pointer', 'fg:#fc413a bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#fc413a bold'), # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
])


class ISM:

    def __init__(self):
        signal(SIGINT, self.shutdown)
        signal(SIGTERM, self.shutdown)

        self.hosts = list()
        self.ssh_config_path = Path('~/.ssh/config').expanduser()
        self.check_if_ssh_config_exists()
        self.load_ssh_hosts()

    def check_if_ssh_config_exists(self):
        if not self.ssh_config_path.exists():
            print('No SSH config file detected at ' + self.ssh_config_path + '. Aborting.')
            sys.exit(1)

    def load_ssh_hosts(self):
        self.hosts = list()
        self.parse_config(self.ssh_config_path)
        self.hosts.sort()
    
    def parse_config(self, config_file_path):
        path = Path(config_file_path).expanduser()
        if path.exists():
            with path.open() as f:
                ssh_config = f.read()
                self.find_hosts(ssh_config)
                self.find_includes(ssh_config)

    def find_hosts(self, config):
        new_hosts = findall(r"Host ((?!\*).*)", config)

        for hostLine in new_hosts:
            self.hosts.extend(hostLine.split(' '))

    def find_includes(self, config):
        include_lines = findall(r"Include (.*)", config)
        for include_line in include_lines:
            for path in include_line.split():
                new_path = Path(path).expanduser()
                if new_path.is_absolute():
                    self.parse_config(path)
                else:
                    self.parse_config(self.ssh_config_path.parent / path)


    def run(self):
        selected_host = (
            questionary.select(
                "Select a Host to connect",
                choices=self.hosts,
                style=custom_style_fancy,
                qmark= ""
            ).ask()
        )

        system('ssh %s' % selected_host)
    
    def shutdown(self):
        sys.exit(0)
    

def main():
    ism = ISM()
    ism.run()

if __name__ == '__main__':
    main()
