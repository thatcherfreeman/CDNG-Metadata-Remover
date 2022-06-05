# CDNG Camera Model Tag Remover

Blackmagic DaVinci Resolve has a quirk that for the BMMCC camera (and presumably Blackmagic's other CDNG recording cameras), the software applies an incorrect log curve when decoding the RAW files. This is demonstrable by recording two clips of the same scene with different shutter speeds and trying to match the exposures in post using any of the scene referred tools in Resolve. However, if you strip out the `UniqueCameraModel` tag, Resolve behaves as exected.

The python tool in this repository can be pointed to a directory of CDNG clip folders and will go through every frame to remove this metadata tag, powered by Exiftool. You should back up your footage before running this program, and give it a lot of time to run because it's truthfully pretty slow.