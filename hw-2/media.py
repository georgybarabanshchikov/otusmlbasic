import datetime
from pathlib import Path
import urllib.request


class File:
    data = bytes
    path = ""
    name = ""
    extension = ""
    created = datetime.time
    modified = datetime.time
    last_open = datetime.time
    owner = ""
    permissions = ""

    def __init__(self, data, path, name, extension, created, modified, last_opened, owner, permission):
        self.data = data
        self.name = name
        self.path = path
        self.extension = extension
        self.created = created
        self.modified = modified
        self.last_opened = last_opened
        self.owner = owner
        self.permission = permission

    def create(self):
        pass

    def save_to_file(self, path):
        p = Path(path)
        p.write_bytes(self.data)

    def delete(self):
        p = Path(self.path)
        p.unlink()

    def upload_from_url(self, path):
        self.data = urllib.request.urlopen(path).read().decode()


#---------
class AudioFile(File):
    codec = ""
    duration = 0



# --------базовый класс для какого-то медиа файла
class MediaFile(File):
    x_resolution = 0
    y_resolution = 0
    has_alpha = False

    def preview(self):
        pass;


# -------------------------
class ImageFile(MediaFile):
    colour_space = "RGB"

    def _show_image(self):
        pass;

    def preview(self):
        self._show_image()


# -------------------------
class VideoFile(MediaFile):
    codec = ""
    duration = 0

    def _play_video(self):
        pass;

    def preview(self):
        self._play_video()
