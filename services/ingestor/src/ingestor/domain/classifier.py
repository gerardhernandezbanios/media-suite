# domain/classifier.py

from ingestor.domain.file_inspector import FileInfo


class Classifier:
    """
    Decide la categoría final de un archivo según su FileInfo.
    """

    IMAGE = "images"
    VIDEO = "videos"
    ANIMATION = "animations"
    ARCHIVE = "archives"
    DIRECTORY = "directories"
    UNSUPPORTED = "unsupported"

    def classify(self, info: FileInfo) -> str:
        if info.is_directory:
            return self.DIRECTORY

        if info.is_archive:
            return self.ARCHIVE

        if info.media_type.is_image():
            return self.IMAGE

        if info.media_type.is_video():
            return self.VIDEO

        if info.media_type.is_animation():
            return self.ANIMATION

        return self.UNSUPPORTED
