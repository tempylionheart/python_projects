Python 3.5.0 |Anaconda 2.4.0 (64-bit)| (default, Oct 20 2015, 07:26:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from os import chdir
>>> chdir("D:\\gitrepos\\PythonProjects")
>>> from rand_file import rand_file
>>> rand_file('E:\\xDocuments\\Anime')
Building file list...
File list complete...
1541 files in list...
Picking a random file from the list...
b'\\Bleach\\Season 8 Arrancar The Fierce Fight (2007\xe2\x80\x932008)\\[DB]_Bleach_162_[A75BCF3D].avi'
<rand_file.rand_file object at 0x000000525EAE77F0>
>>> myFiles = rand_file('E:\\xDocuments\\Anime')
Building file list...
File list complete...
1541 files in list...
Picking a random file from the list...
b'\\Yu Yu Hakusho Season 2 (026-066)\\Subs\\Yu Yu Hakusho - 058 - Wielder of the Dragon.ssa'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\Yozakura Quartet\\[SubDesu] Yozakura Quartet 01 - Hoshi no Umi (1280x720)[794dde3b].mkv'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\Yu-Gi-Oh!\\Yu-Gi-Oh! Season I  (1-49)\\Yu-Gi-Oh 1x29 - Duel Indentity (Part 1).avi'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\Naruto Shippuden\\Season 12 (2012) 243-275\\[HorribleSubs] Naruto Shippuuden - 248 [720p].mkv'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\Bleach\\Season 14 Arrancar Downfall (2010\xe2\x80\x932011)\\[DB]_Bleach_269_[FD6CF682].avi'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\One Piece\\Season 9 (2006-2007) 264-336\\[K-F]_One_Piece_271_[ACE93631].mp4'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\Naruto Shippuden\\Season 13 (2012) 276-298\\Filler 284-289 Extensions to the war arc.txt'
>>> myFiles.re_roll()
Picking a random file from the list...
b'\\One Piece\\Season 1 (1999-2001) 1-62\\[K-F]_One_Piece_003_[34671B30].mp4'
>>> 