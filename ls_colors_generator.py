#!/usr/bin/env python
# -*- coding: utf-8 -*-

# View this file with a 4-space-to-tab ratio.
def get_colors():

	FORMAT_COLORS = {
		LEFT		: "",			# Sequence to print *before* outputting a file name.
		RIGHT		: "",			# Sequence to print *after* outputting a file name.
		END			: "\x1b[0m",	# Sequence to print *after* the command executes.
		RESET		: "\x1b[0m"		# Sequence to print *after* the command executes. (functionally identical)
	}

	# The color_char(fg, bg, char, other) function takes arguments and formats them into a valid
	# LS_COLORS format specifier. FG denotes foreground (it is required). BG denotes background;
	# in order to disable the background set it to -1. The char argument is the character code for
	# the character that must be printed before the filename in ls. The "other" argument denotes
	# any escape codes to print after the main fg/bg sequence (e.g. bold, italic formatters).
	# ^^cc is an alias for color_char.
	SPECIAL = {
		NORMAL 		: "",							# Should be left blank. Used as a fallback for everything else.
		FILE		: color_char(48,-1,0xE612),		# Normal file, or one that does not have a color associated with it.
		DIRECTORY	: color_char(29,-1,0xE5FE),		# A folder.
		LINK		: color_char(147,-1,0xF178),	# Any kind of link.
		ORPHAN		: color_char(232, 197, 0xF12A),	# An "orphaned" inode. Should be set to an error condition.
		MISSING		: color_char(232, 197,ord("?")),# A "missing" inode. Should be set to an error condition.
		PIPE		: color_char(115,-1,0xF25A),	# A named pipe.
		SOCKET		: color_char(140,-1,0xF135),	# Honestly not sure what this is, so it must not appear much. Not needed probably.
		BLOCKDEV	: color_char(178,-1,0xF069),	# A block device (e.g. /dev/sda)
		CHARDEV		: color_char(178,-1,0xF069),	# A character device (e.g. /dev/random)
		DOOR		: color_char(84,-1,0xE5FE),		# Client-server communication door. Not needed.
		EXEC		: color_char(27,-1,0xF135),		# An executable file.
		SETUID		: "",							# Set UID upon execution
		SETGID		: "",							# Set GID upon execution
		STICKY		: color_char(230,-1,0xE612),	# Sticky bit set.
		OTHERWRITE	: color_char(230,-1,0xE612),	# Writable by others than the owner + root.
		STOTHERWRITE: color_char(230,-1,0xE612),	# Sticky, but writable by others than the owner + root.
	}

	EXTENSION_LIST = {
		"*bin":			cc(155, -1, 0xF471),
		"*boot":			cc(27,	-1,	0xF0A0),
		"*dev":			cc(220,	-1, 0xE5FC),
		"*etc":			cc(55,	-1, 0xF0AD),
		"*home":			cc(226,	-1, 0xF015),
		"*lost+found":	cc(165,	-1, 0xF118),
		"*mnt":			cc(129,	-1, 0xF0A0),
		"*opt":			cc(195,	-1, 0xF0AD),
		"*proc":			cc(250,	-1,	0xF0AD),
		"*root":			cc(199,	-1,	0xE26E),
		"*sbin":			cc(160, -1, 0xF471),
		"*sys":			cc(254, -1,	0xF2DB),
		"*usr":			cc(189, -1, 0xF0C0),
		"*var":			cc(120, -1, ord("?")),

		"*README":		cc(220, -1, 0xE714),
		"*README.rst":	cc(220, -1, 0xE714),
		"*LICENSE":		cc(220, -1, 0xE714),
		"*COPYING":		cc(220, -1, 0xE714),
		"*INSTALL":		cc(220, -1, 0xE714),
		"*COPYRIGHT":	cc(220, -1, 0xE714),
		"*AUTHORS":		cc(220, -1, 0xE714),
		"*HISTORY":		cc(220, -1, 0xE714),
		"*CONTRIBUTORS":cc(220, -1, 0xE714),
		"*PATENTS":		cc(220, -1, 0xE714),
		"*VERSION":		cc(220, -1, 0xE714),
		"*NOTICE":		cc(220, -1, 0xE714),
		"*CHANGES":		cc(220, -1, 0xE714),

		"*package.json":			cc(161, -1, 0xE71E),
		"*package-lock.json":			cc(161, -1, 0xE71E),
		"*npm-shrinkwrap.json":			cc(161, -1, 0xE71E),
		"*yarn.lock":			cc(161, -1, 0xE71E),
		"*bower.json":			cc(220, -1, 0xE61A),
		"*composer.json":			cc(220, -1, 0xE783),
		"*composer.lock":			cc(220, -1, 0xE783),
		"*.json":		cc(178, -1, 0xE60B),
		"*Gruntfile.coffee":			cc(166, -1, 0xE74C),
		"*Gruntfile.js":			cc(166, -1, 0xE74C),
		"*gulpfile.js":			cc(204, -1, 0xE763),
		"*.coffee":		cc(74, -1, 0xE61B, other="1"),
		"*.js":			cc(74, -1, 0xE60C, other="1"),

		".log":			cc(190, -1, 0xE714),
		".txt":			cc(253, -1, 0xE714),
		".etx":			cc(184, -1, 0xE60E),
		".info":		cc(184, -1, 0xE60E),
		".markdown":	cc(184, -1, 0xE60E),
		".md":			cc(184, -1, 0xE73E),
		".mkd":			cc(184, -1, 0xE60E),
		".nfo":			cc(184, -1, 0xE60E),
		".pod":			cc(184, -1, 0xE60E),
		".tex":			cc(184, -1, 0xE60E),
		".textile":		cc(184, -1, 0xE60E),
		".msg":			cc(178, -1, 0xE60B),
		".pgn":			cc(178, -1, 0xE60B),
		".rss":			cc(178, -1, 0xE60B),
		".xml":			cc(178, -1, 0xE60B),
		".yml":			cc(178, -1, 0xE60B),
		".RData":		cc(178, -1, 0xE60B),
		".rdata":		cc(178, -1, 0xE60B),
		".cbr":			cc(141, -1, 0xE299),
		".cbz":			cc(141, -1, 0xE299),
		".chm":			cc(141, -1, 0xE299),
		".djvu":		cc(141, -1, 0xE299),
		".pdf":			cc(141, -1, 0xF411),
		".PDF":			cc(141, -1, 0xF411),
		".docm":		cc(111, -1, 0xF1C2, other="4"),
		".doc":			cc(111, -1, 0xF1C2),
		".docx":		cc(111, -1, 0xF1C2),
		".eps":			cc(111, -1, 0xF1C2),
		".ps":			cc(111, -1, 0xF1C2),
		".odb":			cc(111, -1, 0xF1C2),
		".odt":			cc(111, -1, 0xF1C2),
		".rtf":			cc(111, -1, 0xF035),
		".odp":			cc(166, -1, 0xF035),
		".pps":			cc(166, -1, 0xF1C4),
		".ppt":			cc(166, -1, 0xF1C4),
		".pptx":		cc(166, -1, 0xF1C4),
		".ppts":		cc(166, -1, 0xF1C4),
		".pptxm":		cc(166, -1, 0xF1C4, other="4"),
		".pptsm":		cc(166, -1, 0xF1C4, other="4"),
		".csv":			cc(78, -1, 0xF1C0),
		".ods":			cc(112, -1, 0xF1C3),
		".xla":			cc(76, -1, 0xF1C3),
		".xls":			cc(112, -1, 0xF1C3),
		".xlsx":		cc(112, -1, 0xF1C3),
		".xlsxm":		cc(112, -1, 0xF1C3, other="4"),
		".xltm":		cc(73, -1, 0xF1C3, other="4"),
		".xltx":		cc(73, -1, 0xF1C3),
		"*cfg":			cc(1, -1, 0xF0AD),
		"*conf":		cc(1, -1, 0xF0AD),
		"*rc":			cc(1, -1, 0xF0AD),
		".ini":			cc(1, -1, 0xF0AD),
		".viminfo":		cc(1, -1, 0xF0AD),
		".pcf":			cc(1, -1, 0xF0AD),
		".psf":			cc(1, -1, 0xF0AD),
		".git":			cc(197, -1, 0xE702),
		".gitignore":	cc(240, -1, 0xE702),
		".gitattributes":cc(240, -1, 0xE702),
		".gitmodules":	cc(240, -1, 0xE702),
		".awk":			cc(172, -1, 0xF120),
		".bash":		cc(172, -1, 0xF120),
		".bat":			cc(172, -1, 0xF120),
		".BAT":			cc(172, -1, 0xF120),
		".sed":			cc(172, -1, 0xF120),
		".sh":			cc(172, -1, 0xF120),
		".zsh":			cc(172, -1, 0xF120),
		".vim":			cc(172, -1, 0xE62B),
		".ahk":			cc(41, -1, 0xF120),
		".py":			cc(41, -1, 0xE606),
		".pl":			cc(208, -1, 0xE769, other="1"),
		".pm":			cc(208, -1, 0xE769),
		".PL":			cc(160, -1, 0xE769),
		".t":			cc(114, -1, 0xE769),
		".msql":		cc(222, -1, 0xE229),
		".mysql":		cc(222, -1, 0xE229),
		".pgsql":		cc(222, -1, 0xF1C0),
		".sql":			cc(222, -1, 0xF1C0),
		".tcl":			cc(64, -1, 0xE7C4, other="1"),
		".r":			cc(49, -1, ord("R")),
		".R":			cc(49, -1, ord("R")),
		".gs":			cc(81, -1, ord("G")),
		".asm":			cc(81, -1, 0xE79D),
		".cl":			cc(81, -1, 0xE768),
		".lisp":		cc(81, -1, 0xE768),
		".lua":			cc(81, -1, 0xE620),
		".moon":		cc(81, -1, 0xF186),
		".c":			cc(81, -1, 0xE61E),
		".C":			cc(81, -1, 0xE61E),
		".h":			cc(110, -1, 0xE61E),
		".H":			cc(110, -1, 0xE61E),
		".tcc":			cc(110, -1, 0xE61E),
		".c++":			cc(81, -1, 0xE61D),
		".h++":			cc(110, -1, 0xE61D),
		".hpp":			cc(110, -1, 0xE61D),
		".hxx":			cc(110, -1, 0xE61D),
		".ii":			cc(110, -1, 0xE61D),
		".M":			cc(110, -1, 0xE61E),
		".m":			cc(110, -1, 0xE61E),
		".cc":			cc(81, -1, ord("#")),
		".cs":			cc(81, -1, ord("#")),
		".cp":			cc(81, -1, ord("#")),
		".cpp":			cc(81, -1, 0xE61D),
		".cxx":			cc(81, -1, 0xE61D),
		".cr":			cc(81, -1, 0xE739),
		".go":			cc(81, -1, 0xE724),
		".f":			cc(81, -1, ord("F")),
		".for":			cc(81, -1, ord("F")),
		".ftn":			cc(81, -1, ord("F")),
		".s":			cc(110, -1, 0xE79D),
		".S":			cc(110, -1, 0xE79D),
		".rs":			cc(81, -1, 0xE7A8),
		".sx":			cc(81, -1, ord("?")),
		".hi":			cc(110, -1, ord("I")),
		".hs":			cc(81, -1, 0xE61F),
		".lhs":			cc(81, -1, 0xE61F),
		".pyc":			cc(240, -1, 0xE606),
		".css":			cc(125, -1, 0xE749, other="1"),
		".less":		cc(125, -1, 0xE758, other="1"),
		".sass":		cc(125, -1, 0xE74B, other="1"),
		".scss":		cc(125, -1, 0xE603, other="1"),
		".htm":			cc(125, -1, 0xE736, other="1"),
		".html":		cc(125, -1, 0xE736, other="1"),
		".jhtm":		cc(125, -1, 0xE60E, other="1"),
		".mht":			cc(125, -1, 0xE60E, other="1"),
		".eml":			cc(125, -1, 0xE60E, other="1"),
		".mustache":	cc(125, -1, 0xE60F, other="1"),
		".java":		cc(74, -1, 0xE61B, other="1"),
		".jsm":			cc(74, -1, 0xE60C, other="1"),
		".jsp":			cc(74, -1, 0xE60C, other="1"),
		".php":			cc(81, -1, 0xE608),
		".ctp":			cc(81, -1, 0xE608),
		".twig":		cc(81, -1, 0xE61C),
		".vb":			cc(81, -1, ord("V")),
		".vba":			cc(81, -1, ord("V")),
		".vbs":			cc(81, -1, ord("V")),
		"*Dockerfile":	cc(155, -1, 0xE7B0),
		".dockerignore":cc(240, -1, 0xE7B0),
		"*Makefile":	cc(155, -1, 0xF0AD),
		"*MANIFEST":	cc(243, -1, 0xF0AD),
		"*pm_to_blib":	cc(240, -1, 0xF0AD),
		".am":			cc(242, -1, 0xF0AD),
		".in":			cc(242, -1, 0xF0AD),
		".hin":			cc(242, -1, 0xF0AD),
		".scan":		cc(242, -1, 0xF0AD),
		".m4":			cc(242, -1, 0xF0AD),
		".old":			cc(242, -1, 0xF0AD),
		".out":			cc(242, -1, 0xF0AD),
		".SKIP":		cc(244, -1, 0xF0AD),
		".diff":		cc(232, 197, 0xF467, other="1"),
		".patch":		cc(232, 197, 0xF467, other="1"),
		".bmp":			cc(97, -1, 0xE60D),
		".tiff":		cc(97, -1, 0xE60D),
		".tif":			cc(97, -1, 0xE60D),
		".TIFF":		cc(97, -1, 0xE60D),
		".cdr":			cc(97, -1, 0xE60D),
		".gif":			cc(97, -1, 0xE60D),
		".ico":			cc(97, -1, 0xE60D),
		".jpeg":		cc(97, -1, 0xE60D),
		".JPG":			cc(97, -1, 0xE60D),
		".jpg":			cc(97, -1, 0xE60D),
		".nth":			cc(97, -1, 0xE60D),
		".png":			cc(97, -1, 0xE60D),
		".psd":			cc(97, -1, 0xE7B8),
		".xpm":			cc(97, -1, 0xE60D),
		".ai":			cc(99, -1, 0xE7B4),
		".eps":			cc(99, -1, 0xE60D),
		".epsf":		cc(99, -1, 0xE60D),
		".drw":			cc(99, -1, 0xE60D),
		".ps":			cc(99, -1, 0xE7B8),
		".svg":			cc(99, -1, 0xE60D),
		".avi":			cc(114, -1, 0xE60D),
		".divx":		cc(114, -1, 0xE60D),
		".IFO":			cc(114, -1, 0xE60D),
		".m2v":			cc(114, -1, 0xE60D),
		".m4v":			cc(114, -1, 0xE60D),
		".mkv":			cc(114, -1, 0xE60D),
		".MOV":			cc(114, -1, 0xE60D),
		".mov":			cc(114, -1, 0xE60D),
		".mp4":			cc(114, -1, 0xE60D),
		".mpeg":		cc(114, -1, 0xE60D),
		".mpg":			cc(114, -1, 0xE60D),
		".ogm":			cc(114, -1, 0xE60D),
		".rmvb":		cc(114, -1, 0xE60D),
		".sample":		cc(114, -1, 0xE60D),
		".wmv":			cc(114, -1, 0xE60D),
		".3g2":			cc(115, -1, 0xF10B),
		".3gp":			cc(115, -1, 0xF10B),
		".gp3":			cc(115, -1, 0xF10B),
		".webm":		cc(115, -1, 0xF10B),
		".gp4":			cc(115, -1, 0xF10B),
		".asf":			cc(115, -1, 0xF10B),
		".flv":			cc(115, -1, 0xF10B),
		".ts":			cc(115, -1, 0xF10B),
		".ogv":			cc(115, -1, 0xF10B),
		".f4v":			cc(115, -1, 0xF10B),
		".VOB":			cc(115, -1, 0xE60D, other="1"),
		".vob":			cc(115, -1, 0xE60D, other="1"),
		".3ga":			cc(137, -1, 0xF025, other="1"),
		".S3M":			cc(137, -1, 0xF025, other="1"),
		".aac":			cc(137, -1, 0xF025, other="1"),
		".au":			cc(137, -1, 0xF025, other="1"),
		".dat":			cc(137, -1, 0xF025, other="1"),
		".dts":			cc(137, -1, 0xF025, other="1"),
		".fcm":			cc(137, -1, 0xF025, other="1"),
		".m4a":			cc(137, -1, 0xF025, other="1"),
		".mid":			cc(137, -1, 0xF025, other="1"),
		".midi":		cc(137, -1, 0xF025, other="1"),
		".mod":			cc(137, -1, 0xF025, other="1"),
		".mp3":			cc(137, -1, 0xF025, other="1"),
		".mp4a":		cc(137, -1, 0xF025, other="1"),
		".oga":			cc(137, -1, 0xF025, other="1"),
		".ogg":			cc(137, -1, 0xF025, other="1"),
		".opus":		cc(137, -1, 0xF025, other="1"),
		".s3m":			cc(137, -1, 0xF025, other="1"),
		".sid":			cc(137, -1, 0xF025, other="1"),
		".wma":			cc(137, -1, 0xF025, other="1"),
		".ape":			cc(136, -1, 0xF025, other="1"),
		".aiff":		cc(136, -1, 0xF025, other="1"),
		".cda":			cc(136, -1, 0xF025, other="1"),
		".flac":		cc(136, -1, 0xF025, other="1"),
		".alac":		cc(136, -1, 0xF025, other="1"),
		".midi":		cc(136, -1, 0xF025, other="1"),
		".pcm":			cc(136, -1, 0xF025, other="1"),
		".wav":			cc(136, -1, 0xF025, other="1"),
		".wv":			cc(136, -1, 0xF025, other="1"),
		".wvc":			cc(136, -1, 0xF025, other="1"),
		".afm":			cc(66, -1, 0xF031),
		".fon":			cc(66, -1, 0xF031),
		".fnt":			cc(66, -1, 0xF031),
		".pfb":			cc(66, -1, 0xF031),
		".pfm":			cc(66, -1, 0xF031),
		".ttf":			cc(66, -1, 0xF031),
		".otf":			cc(66, -1, 0xF031),
		".PFA":			cc(66, -1, 0xF031),
		".pfa":			cc(66, -1, 0xF031),
		".7z":			cc(40, -1, 0xF187),
		".a":			cc(40, -1, 0xF187),
		".arj":			cc(40, -1, 0xF187),
		".bz2":			cc(40, -1, 0xF187),
		".cpio":		cc(40, -1, 0xF187),
		".gz":			cc(40, -1, 0xF187),
		".lrz":			cc(40, -1, 0xF187),
		".lz":			cc(40, -1, 0xF187),
		".lzma":		cc(40, -1, 0xF187),
		".lzo":			cc(40, -1, 0xF187),
		".rar":			cc(40, -1, 0xF187),
		".s7z":			cc(40, -1, 0xF187),
		".sz":			cc(40, -1, 0xF187),
		".tar":			cc(40, -1, 0xF187),
		".tgz":			cc(40, -1, 0xF187),
		".xz":			cc(40, -1, 0xF187),
		".zip":			cc(40, -1, 0xF187),
		".zipx":		cc(40, -1, 0xF187),
		".zoo":			cc(40, -1, 0xF187),
		".zpaq":		cc(40, -1, 0xF187),
		".zz":			cc(40, -1, 0xF187),
		".Z":			cc(40, -1, 0xF187),
		".z":			cc(40, -1, 0xF187),
		".apk":			cc(40, -1, 0xF487),
		".deb":			cc(40, -1, 0xF487),
		".rpm":			cc(40, -1, 0xF487),
		".jad":			cc(40, -1, 0xF487),
		".jar":			cc(40, -1, 0xF487),
		".cab":			cc(40, -1, 0xF487),
		".pak":			cc(40, -1, 0xF487),
		".pk3":			cc(40, -1, 0xF487),
		".vdf":			cc(40, -1, 0xF487),
		".vpk":			cc(40, -1, 0xF487),
		".bsp":			cc(40, -1, 0xF487),
		".dmg":			cc(40, -1, 0xF487),
		".r00":			cc(239, -1, 0xE601),
		".r01":			cc(239, -1, 0xE601),
		".r02":			cc(239, -1, 0xE601),
		".r03":			cc(239, -1, 0xE601),
		".r04":			cc(239, -1, 0xE601),
		".r05":			cc(239, -1, 0xE601),
		".r06":			cc(239, -1, 0xE601),
		".r07":			cc(239, -1, 0xE601),
		".r08":			cc(239, -1, 0xE601),
		".r09":			cc(239, -1, 0xE601),
		".r10":			cc(239, -1, 0xE601),
		".r100":		cc(239, -1, 0xE601),
		".r101":		cc(239, -1, 0xE601),
		".r102":		cc(239, -1, 0xE601),
		".r103":		cc(239, -1, 0xE601),
		".r104":		cc(239, -1, 0xE601),
		".r105":		cc(239, -1, 0xE601),
		".r106":		cc(239, -1, 0xE601),
		".r107":		cc(239, -1, 0xE601),
		".r108":		cc(239, -1, 0xE601),
		".r109":		cc(239, -1, 0xE601),
		".r11":			cc(239, -1, 0xE601),
		".r110":		cc(239, -1, 0xE601),
		".r111":		cc(239, -1, 0xE601),
		".r112":		cc(239, -1, 0xE601),
		".r113":		cc(239, -1, 0xE601),
		".r114":		cc(239, -1, 0xE601),
		".r115":		cc(239, -1, 0xE601),
		".r116":		cc(239, -1, 0xE601),
		".r12":			cc(239, -1, 0xE601),
		".r13":			cc(239, -1, 0xE601),
		".r14":			cc(239, -1, 0xE601),
		".r15":			cc(239, -1, 0xE601),
		".r16":			cc(239, -1, 0xE601),
		".r17":			cc(239, -1, 0xE601),
		".r18":			cc(239, -1, 0xE601),
		".r19":			cc(239, -1, 0xE601),
		".r20":			cc(239, -1, 0xE601),
		".r21":			cc(239, -1, 0xE601),
		".r22":			cc(239, -1, 0xE601),
		".r25":			cc(239, -1, 0xE601),
		".r26":			cc(239, -1, 0xE601),
		".r27":			cc(239, -1, 0xE601),
		".r28":			cc(239, -1, 0xE601),
		".r29":			cc(239, -1, 0xE601),
		".r30":			cc(239, -1, 0xE601),
		".r31":			cc(239, -1, 0xE601),
		".r32":			cc(239, -1, 0xE601),
		".r33":			cc(239, -1, 0xE601),
		".r34":			cc(239, -1, 0xE601),
		".r35":			cc(239, -1, 0xE601),
		".r36":			cc(239, -1, 0xE601),
		".r37":			cc(239, -1, 0xE601),
		".r38":			cc(239, -1, 0xE601),
		".r39":			cc(239, -1, 0xE601),
		".r40":			cc(239, -1, 0xE601),
		".r41":			cc(239, -1, 0xE601),
		".r42":			cc(239, -1, 0xE601),
		".r43":			cc(239, -1, 0xE601),
		".r44":			cc(239, -1, 0xE601),
		".r45":			cc(239, -1, 0xE601),
		".r46":			cc(239, -1, 0xE601),
		".r47":			cc(239, -1, 0xE601),
		".r48":			cc(239, -1, 0xE601),
		".r49":			cc(239, -1, 0xE601),
		".r50":			cc(239, -1, 0xE601),
		".r51":			cc(239, -1, 0xE601),
		".r52":			cc(239, -1, 0xE601),
		".r53":			cc(239, -1, 0xE601),
		".r54":			cc(239, -1, 0xE601),
		".r55":			cc(239, -1, 0xE601),
		".r56":			cc(239, -1, 0xE601),
		".r57":			cc(239, -1, 0xE601),
		".r58":			cc(239, -1, 0xE601),
		".r59":			cc(239, -1, 0xE601),
		".r60":			cc(239, -1, 0xE601),
		".r61":			cc(239, -1, 0xE601),
		".r62":			cc(239, -1, 0xE601),
		".r63":			cc(239, -1, 0xE601),
		".r64":			cc(239, -1, 0xE601),
		".r65":			cc(239, -1, 0xE601),
		".r66":			cc(239, -1, 0xE601),
		".r67":			cc(239, -1, 0xE601),
		".r68":			cc(239, -1, 0xE601),
		".r69":			cc(239, -1, 0xE601),
		".r69":			cc(239, -1, 0xE601),
		".r70":			cc(239, -1, 0xE601),
		".r71":			cc(239, -1, 0xE601),
		".r72":			cc(239, -1, 0xE601),
		".r73":			cc(239, -1, 0xE601),
		".r74":			cc(239, -1, 0xE601),
		".r75":			cc(239, -1, 0xE601),
		".r76":			cc(239, -1, 0xE601),
		".r77":			cc(239, -1, 0xE601),
		".r78":			cc(239, -1, 0xE601),
		".r79":			cc(239, -1, 0xE601),
		".r80":			cc(239, -1, 0xE601),
		".r81":			cc(239, -1, 0xE601),
		".r82":			cc(239, -1, 0xE601),
		".r83":			cc(239, -1, 0xE601),
		".r84":			cc(239, -1, 0xE601),
		".r85":			cc(239, -1, 0xE601),
		".r86":			cc(239, -1, 0xE601),
		".r87":			cc(239, -1, 0xE601),
		".r88":			cc(239, -1, 0xE601),
		".r89":			cc(239, -1, 0xE601),
		".r90":			cc(239, -1, 0xE601),
		".r91":			cc(239, -1, 0xE601),
		".r92":			cc(239, -1, 0xE601),
		".r93":			cc(239, -1, 0xE601),
		".r94":			cc(239, -1, 0xE601),
		".r95":			cc(239, -1, 0xE601),
		".r96":			cc(239, -1, 0xE601),
		".r97":			cc(239, -1, 0xE601),
		".r98":			cc(239, -1, 0xE601),
		".r99":			cc(239, -1, 0xE601),
		".zx00":		cc(239, -1, 0xE601),
		".zx01":		cc(239, -1, 0xE601),
		".zx02":		cc(239, -1, 0xE601),
		".zx03":		cc(239, -1, 0xE601),
		".zx04":		cc(239, -1, 0xE601),
		".zx05":		cc(239, -1, 0xE601),
		".zx06":		cc(239, -1, 0xE601),
		".zx07":		cc(239, -1, 0xE601),
		".zx08":		cc(239, -1, 0xE601),
		".zx09":		cc(239, -1, 0xE601),
		".zx10":		cc(239, -1, 0xE601),
		".zx11":		cc(239, -1, 0xE601),
		".zx12":		cc(239, -1, 0xE601),
		".zx13":		cc(239, -1, 0xE601),
		".zx14":		cc(239, -1, 0xE601),
		".zx15":		cc(239, -1, 0xE601),
		".zx16":		cc(239, -1, 0xE601),
		".zx17":		cc(239, -1, 0xE601),
		".zx18":		cc(239, -1, 0xE601),
		".zx19":		cc(239, -1, 0xE601),
		".zx20":		cc(239, -1, 0xE601),
		".zx21":		cc(239, -1, 0xE601),
		".zx22":		cc(239, -1, 0xE601),
		".zx25":		cc(239, -1, 0xE601),
		".zx26":		cc(239, -1, 0xE601),
		".zx27":		cc(239, -1, 0xE601),
		".zx28":		cc(239, -1, 0xE601),
		".zx29":		cc(239, -1, 0xE601),
		".zx30":		cc(239, -1, 0xE601),
		".zx31":		cc(239, -1, 0xE601),
		".zx32":		cc(239, -1, 0xE601),
		".zx33":		cc(239, -1, 0xE601),
		".zx34":		cc(239, -1, 0xE601),
		".zx35":		cc(239, -1, 0xE601),
		".zx36":		cc(239, -1, 0xE601),
		".zx37":		cc(239, -1, 0xE601),
		".zx38":		cc(239, -1, 0xE601),
		".zx39":		cc(239, -1, 0xE601),
		".zx40":		cc(239, -1, 0xE601),
		".zx41":		cc(239, -1, 0xE601),
		".zx42":		cc(239, -1, 0xE601),
		".zx43":		cc(239, -1, 0xE601),
		".zx44":		cc(239, -1, 0xE601),
		".zx45":		cc(239, -1, 0xE601),
		".zx46":		cc(239, -1, 0xE601),
		".zx47":		cc(239, -1, 0xE601),
		".zx48":		cc(239, -1, 0xE601),
		".zx49":		cc(239, -1, 0xE601),
		".zx50":		cc(239, -1, 0xE601),
		".zx51":		cc(239, -1, 0xE601),
		".zx52":		cc(239, -1, 0xE601),
		".zx53":		cc(239, -1, 0xE601),
		".zx54":		cc(239, -1, 0xE601),
		".zx55":		cc(239, -1, 0xE601),
		".zx56":		cc(239, -1, 0xE601),
		".zx57":		cc(239, -1, 0xE601),
		".zx58":		cc(239, -1, 0xE601),
		".zx59":		cc(239, -1, 0xE601),
		".zx60":		cc(239, -1, 0xE601),
		".zx61":		cc(239, -1, 0xE601),
		".zx62":		cc(239, -1, 0xE601),
		".zx63":		cc(239, -1, 0xE601),
		".zx64":		cc(239, -1, 0xE601),
		".zx65":		cc(239, -1, 0xE601),
		".zx66":		cc(239, -1, 0xE601),
		".zx67":		cc(239, -1, 0xE601),
		".zx68":		cc(239, -1, 0xE601),
		".zx69":		cc(239, -1, 0xE601),
		".zx69":		cc(239, -1, 0xE601),
		".zx70":		cc(239, -1, 0xE601),
		".zx71":		cc(239, -1, 0xE601),
		".zx72":		cc(239, -1, 0xE601),
		".zx73":		cc(239, -1, 0xE601),
		".zx74":		cc(239, -1, 0xE601),
		".zx75":		cc(239, -1, 0xE601),
		".zx76":		cc(239, -1, 0xE601),
		".zx77":		cc(239, -1, 0xE601),
		".zx78":		cc(239, -1, 0xE601),
		".zx79":		cc(239, -1, 0xE601),
		".zx80":		cc(239, -1, 0xE601),
		".zx81":		cc(239, -1, 0xE601),
		".zx82":		cc(239, -1, 0xE601),
		".zx83":		cc(239, -1, 0xE601),
		".zx84":		cc(239, -1, 0xE601),
		".zx85":		cc(239, -1, 0xE601),
		".zx86":		cc(239, -1, 0xE601),
		".zx87":		cc(239, -1, 0xE601),
		".zx88":		cc(239, -1, 0xE601),
		".zx89":		cc(239, -1, 0xE601),
		".zx90":		cc(239, -1, 0xE601),
		".zx91":		cc(239, -1, 0xE601),
		".zx92":		cc(239, -1, 0xE601),
		".zx93":		cc(239, -1, 0xE601),
		".zx94":		cc(239, -1, 0xE601),
		".zx95":		cc(239, -1, 0xE601),
		".zx96":		cc(239, -1, 0xE601),
		".zx97":		cc(239, -1, 0xE601),
		".zx98":		cc(239, -1, 0xE601),
		".zx99":		cc(239, -1, 0xE601),
		".zx100":		cc(239, -1, 0xE601),
		".zx101":		cc(239, -1, 0xE601),
		".zx102":		cc(239, -1, 0xE601),
		".zx103":		cc(239, -1, 0xE601),
		".zx104":		cc(239, -1, 0xE601),
		".zx105":		cc(239, -1, 0xE601),
		".zx106":		cc(239, -1, 0xE601),
		".zx107":		cc(239, -1, 0xE601),
		".zx108":		cc(239, -1, 0xE601),
		".zx109":		cc(239, -1, 0xE601),
		".zx110":		cc(239, -1, 0xE601),
		".zx111":		cc(239, -1, 0xE601),
		".zx112":		cc(239, -1, 0xE601),
		".zx113":		cc(239, -1, 0xE601),
		".zx114":		cc(239, -1, 0xE601),
		".zx115":		cc(239, -1, 0xE601),
		".zx116":		cc(239, -1, 0xE601),
		".z00":			cc(239, -1, 0xE601),
		".z01":			cc(239, -1, 0xE601),
		".z02":			cc(239, -1, 0xE601),
		".z03":			cc(239, -1, 0xE601),
		".z04":			cc(239, -1, 0xE601),
		".z05":			cc(239, -1, 0xE601),
		".z06":			cc(239, -1, 0xE601),
		".z07":			cc(239, -1, 0xE601),
		".z08":			cc(239, -1, 0xE601),
		".z09":			cc(239, -1, 0xE601),
		".z10":			cc(239, -1, 0xE601),
		".z11":			cc(239, -1, 0xE601),
		".z12":			cc(239, -1, 0xE601),
		".z13":			cc(239, -1, 0xE601),
		".z14":			cc(239, -1, 0xE601),
		".z15":			cc(239, -1, 0xE601),
		".z16":			cc(239, -1, 0xE601),
		".z17":			cc(239, -1, 0xE601),
		".z18":			cc(239, -1, 0xE601),
		".z19":			cc(239, -1, 0xE601),
		".z20":			cc(239, -1, 0xE601),
		".z21":			cc(239, -1, 0xE601),
		".z22":			cc(239, -1, 0xE601),
		".z25":			cc(239, -1, 0xE601),
		".z26":			cc(239, -1, 0xE601),
		".z27":			cc(239, -1, 0xE601),
		".z28":			cc(239, -1, 0xE601),
		".z29":			cc(239, -1, 0xE601),
		".z30":			cc(239, -1, 0xE601),
		".z31":			cc(239, -1, 0xE601),
		".z32":			cc(239, -1, 0xE601),
		".z33":			cc(239, -1, 0xE601),
		".z34":			cc(239, -1, 0xE601),
		".z35":			cc(239, -1, 0xE601),
		".z36":			cc(239, -1, 0xE601),
		".z37":			cc(239, -1, 0xE601),
		".z38":			cc(239, -1, 0xE601),
		".z39":			cc(239, -1, 0xE601),
		".z40":			cc(239, -1, 0xE601),
		".z41":			cc(239, -1, 0xE601),
		".z42":			cc(239, -1, 0xE601),
		".z43":			cc(239, -1, 0xE601),
		".z44":			cc(239, -1, 0xE601),
		".z45":			cc(239, -1, 0xE601),
		".z46":			cc(239, -1, 0xE601),
		".z47":			cc(239, -1, 0xE601),
		".z48":			cc(239, -1, 0xE601),
		".z49":			cc(239, -1, 0xE601),
		".z50":			cc(239, -1, 0xE601),
		".z51":			cc(239, -1, 0xE601),
		".z52":			cc(239, -1, 0xE601),
		".z53":			cc(239, -1, 0xE601),
		".z54":			cc(239, -1, 0xE601),
		".z55":			cc(239, -1, 0xE601),
		".z56":			cc(239, -1, 0xE601),
		".z57":			cc(239, -1, 0xE601),
		".z58":			cc(239, -1, 0xE601),
		".z59":			cc(239, -1, 0xE601),
		".z60":			cc(239, -1, 0xE601),
		".z61":			cc(239, -1, 0xE601),
		".z62":			cc(239, -1, 0xE601),
		".z63":			cc(239, -1, 0xE601),
		".z64":			cc(239, -1, 0xE601),
		".z65":			cc(239, -1, 0xE601),
		".z66":			cc(239, -1, 0xE601),
		".z67":			cc(239, -1, 0xE601),
		".z68":			cc(239, -1, 0xE601),
		".z69":			cc(239, -1, 0xE601),
		".z69":			cc(239, -1, 0xE601),
		".z70":			cc(239, -1, 0xE601),
		".z71":			cc(239, -1, 0xE601),
		".z72":			cc(239, -1, 0xE601),
		".z73":			cc(239, -1, 0xE601),
		".z74":			cc(239, -1, 0xE601),
		".z75":			cc(239, -1, 0xE601),
		".z76":			cc(239, -1, 0xE601),
		".z77":			cc(239, -1, 0xE601),
		".z78":			cc(239, -1, 0xE601),
		".z79":			cc(239, -1, 0xE601),
		".z80":			cc(239, -1, 0xE601),
		".z81":			cc(239, -1, 0xE601),
		".z82":			cc(239, -1, 0xE601),
		".z83":			cc(239, -1, 0xE601),
		".z84":			cc(239, -1, 0xE601),
		".z85":			cc(239, -1, 0xE601),
		".z86":			cc(239, -1, 0xE601),
		".z87":			cc(239, -1, 0xE601),
		".z88":			cc(239, -1, 0xE601),
		".z89":			cc(239, -1, 0xE601),
		".z90":			cc(239, -1, 0xE601),
		".z91":			cc(239, -1, 0xE601),
		".z92":			cc(239, -1, 0xE601),
		".z93":			cc(239, -1, 0xE601),
		".z94":			cc(239, -1, 0xE601),
		".z95":			cc(239, -1, 0xE601),
		".z96":			cc(239, -1, 0xE601),
		".z97":			cc(239, -1, 0xE601),
		".z98":			cc(239, -1, 0xE601),
		".z99":			cc(239, -1, 0xE601),
		".z100":		cc(239, -1, 0xE601),
		".z101":		cc(239, -1, 0xE601),
		".z102":		cc(239, -1, 0xE601),
		".z103":		cc(239, -1, 0xE601),
		".z104":		cc(239, -1, 0xE601),
		".z105":		cc(239, -1, 0xE601),
		".z106":		cc(239, -1, 0xE601),
		".z107":		cc(239, -1, 0xE601),
		".z108":		cc(239, -1, 0xE601),
		".z109":		cc(239, -1, 0xE601),
		".z110":		cc(239, -1, 0xE601),
		".z111":		cc(239, -1, 0xE601),
		".z112":		cc(239, -1, 0xE601),
		".z113":		cc(239, -1, 0xE601),
		".z114":		cc(239, -1, 0xE601),
		".z115":		cc(239, -1, 0xE601),
		".z116":		cc(239, -1, 0xE601),
		".part":		cc(239, -1, 0xE601),
		".dmg":			cc(124, -1, 0xF0A0),
		".iso":			cc(124, -1, 0xF0A0),
		".bin":			cc(124, -1, 0xF0A0),
		".nrg":			cc(124, -1, 0xF0A0),
		".qcow":		cc(124, -1, 0xF0A0),
		".sparseimage":	cc(124, -1, 0xF0A0),
		".toast":		cc(124, -1, 0xF0A0),
		".vcd":			cc(124, -1, 0xF0A0),
		".vmdk":		cc(124, -1, 0xF0A0),
		".accdb":		cc(60, -1, 0xF1C0),
		".accde":		cc(60, -1, 0xF1C0),
		".accdr":		cc(60, -1, 0xF1C0),
		".accdt":		cc(60, -1, 0xF1C0),
		".db":			cc(60, -1, 0xF1C0),
		".fmp12":		cc(60, -1, 0xF1C0),
		".fp7":			cc(60, -1, 0xF1C0),
		".localstorage":cc(60, -1, 0xF1C0),
		".mdb":			cc(60, -1, 0xF1C0),
		".mde":			cc(60, -1, 0xF1C0),
		".sqlite":		cc(60, -1, 0xF1C0),
		".typelib":		cc(60, -1, 0xF1C0),
		".nc":			cc(60, -1, 0xF1C0),
		".pacnew":		cc(33, -1, 0xF0E2),
		".un~":			cc(241, -1, 0xF0E2),
		".orig":		cc(241, -1, 0xF0E2),
		".BUP":			cc(241, -1, 0xF0E2),
		".bak":			cc(241, -1, 0xF0E2),
		".swp":			cc(244, -1, ord("T")),
		".swo":			cc(244, -1, ord("T")),
		".tmp":			cc(244, -1, ord("T")),
		".sassc":		cc(244, -1, ord("T")),
		".pid":			cc(248, -1, 0xF023),
		".state":		cc(248, -1, 0xF023),
		"*lockfile":	cc(248, -1, 0xF023),
		".err":			cc(160, -1, 0xF12A, other="1"),
		".error":		cc(160, -1, 0xF12A, other="1"),
		".stderr":		cc(160, -1, 0xF12A, other="1"),
		".dump":		cc(241, -1, 0xF487),
		".stackdump":	cc(241, -1, 0xF487),
		".zcompdump":	cc(241, -1, 0xF487),
		".zwc":			cc(241, -1, 0xF487),
		".pcap":		cc(29, -1, 0xE765),
		".cap":			cc(29, -1, 0xE765),
		".dmp":			cc(29, -1, 0xE765),
		".DS_Store":	cc(239, -1, 0xF179),
		".localized":	cc(239, -1, 0xF179),
		".CFUserTextEncoding":	cc(239, -1, 0xF179),
		".allow":		cc(112, -1, 0xF00C),
		".deny":		cc(196, -1, 0xF12A),
		".service":		cc(45, -1, 0xF109),
		"*@.service":	cc(45, -1, 0xF109),
		".socket":		cc(45, -1, 0xF109),
		".swap":		cc(45, -1, 0xF109),
		".device":		cc(45, -1, 0xF109),
		".mount":		cc(45, -1, 0xF109),
		".automount":	cc(45, -1, 0xF109),
		".target":		cc(45, -1, 0xF109),
		".path":		cc(45, -1, 0xF109),
		".timer":		cc(45, -1, 0xF109),
		".snapshot":	cc(45, -1, 0xF109),
		".application":	cc(116, -1, 0xE60B),
		".cue":			cc(116, -1, 0xE60B),
		".description":	cc(116, -1, 0xE60B),
		".directory":	cc(116, -1, 0xE60B),
		".m3u":			cc(116, -1, 0xE60B),
		".m3u8":		cc(116, -1, 0xE60B),
		".md5":			cc(116, -1, ord("#")),
		".properties":	cc(116, -1, 0xE60B),
		".sfv":			cc(116, -1, 0xE60B),
		".srt":			cc(116, -1, 0xE60B),
		".theme":		cc(116, -1, 0xE60B),
		".torrent":		cc(116, -1, 0xE60B),
		".urlview":		cc(116, -1, 0xE60B),
		".asc":			cc(192, -1, 0xF084, other="3"),
		".bfe":			cc(192, -1, 0xF084, other="3"),
		".enc":			cc(192, -1, 0xF084, other="3"),
		".gpg":			cc(192, -1, 0xF084, other="3"),
		".signature":	cc(192, -1, 0xF084, other="3"),
		".sig":			cc(192, -1, 0xF084, other="3"),
		".p12":			cc(192, -1, 0xF084, other="3"),
		".pem":			cc(192, -1, 0xF084, other="3"),
		".pgp":			cc(192, -1, 0xF084, other="3"),
		".asc":			cc(192, -1, 0xF084, other="3"),
		".enc":			cc(192, -1, 0xF084, other="3"),
		".sig":			cc(192, -1, 0xF084, other="3"),
		".32x":			cc(213, -1, 0xF11B),
		".cdi":			cc(213, -1, 0xF11B),
		".fm2":			cc(213, -1, 0xF11B),
		".rom":			cc(213, -1, 0xF11B),
		".sav":			cc(213, -1, 0xF11B),
		".st":			cc(213, -1, 0xF11B),
		".a00":			cc(213, -1, 0xF11B),
		".a52":			cc(213, -1, 0xF11B),
		".A64":			cc(213, -1, 0xF11B),
		".a64":			cc(213, -1, 0xF11B),
		".a78":			cc(213, -1, 0xF11B),
		".adf":			cc(213, -1, 0xF11B),
		".atr":			cc(213, -1, 0xF11B),
		".gb":			cc(213, -1, 0xF11B),
		".gba":			cc(213, -1, 0xF11B),
		".gbc":			cc(213, -1, 0xF11B),
		".gel":			cc(213, -1, 0xF11B),
		".gg":			cc(213, -1, 0xF11B),
		".ggl":			cc(213, -1, 0xF11B),
		".j64":			cc(213, -1, 0xF11B),
		".nds":			cc(213, -1, 0xF11B),
		".nes":			cc(213, -1, 0xF11B),
		".sms":			cc(213, -1, 0xF11B),
		".pot":			cc(7, -1, ord("P")),
		".pcb":			cc(7, -1, 0xF493),
		".mm":			cc(7, -1, 0xF035),
		".pod":			cc(7, -1, 0xF035),
		".gbr":			cc(7, -1, 0xF1FC),
		".spl":			cc(7, -1, ord("S")),
		".scm":			cc(7, -1, 0xF1FC),
		".Rproj":		cc(11, -1, 0xF1FC),
		".sis":			cc(7, -1, 0xF10B),
		".1p":			cc(7, -1, 0xF10B),
		".3p":			cc(7, -1, 0xF10B),
		".cnc":			cc(7, -1, 0xF10B),
		".def":			cc(7, -1, 0xF10B),
		".ex":			cc(7, -1, 0xF10B),
		".example":		cc(7, -1, 0xF10B),
		".feature":		cc(7, -1, 0xF10B),
		".ger":			cc(7, -1, 0xF10B),
		".map":			cc(7, -1, 0xF10B),
		".mf":			cc(7, -1, 0xF10B),
		".mfasl":		cc(7, -1, 0xF10B),
		".mi":			cc(7, -1, 0xF10B),
		".mtx":			cc(7, -1, 0xF10B),
		".pc":			cc(7, -1, 0xF10B),
		".pi":			cc(7, -1, 0xF10B),
		".plt":			cc(7, -1, 0xF10B),
		".rb":			cc(1, -1, 0xE739),
		".rdf":			cc(7, -1, 0xF10B),
		".rst":			cc(7, -1, 0xF10B),
		".ru":			cc(7, -1, 0xF10B),
		".sch":			cc(7, -1, 0xF10B),
		".sty":			cc(7, -1, 0xF10B),
		".sug":			cc(7, -1, 0xF10B),
		".t":			cc(7, -1, 0xF10B),
		".tdy":			cc(7, -1, 0xF10B),
		".tfm":			cc(7, -1, 0xF10B),
		".tfnt":		cc(7, -1, 0xF10B),
		".tg":			cc(7, -1, 0xF10B),
		".vcard":		cc(7, -1, 0xF10B),
		".vcf":			cc(7, -1, 0xF10B),
		".xln":			cc(7, -1, 0xF10B)
	}

	return FORMAT_COLORS, SPECIAL, EXTENSION_LIST

# Formats arguments into an LS_COLORS-complete escape sequence.
def color_char(f,b,c,other=""):
	return "m%s\x1b" % ("%s%s " % (color_seq(f,b,other),get_unicode(c)))

cc = color_char

# Formats fg and bg into an escape sequence.
def color_seq(f,b,other):
	if b != -1:
		if other != "":
			return "\x1b[38;5;%i;48;5;%i;%sm" % (f, b, other)
		else:
			return "\x1b[38;5;%i;48;5;%im" % (f, b)
	else:
		if other != "":
			return "\x1b[38;5;%i;%sm" % (f, other)
		else:
			return "\x1b[38;5;%im" % f

# Return a unicode character. Python 2 and 3 complete.
def get_unicode(ch):
	try:
		return unichr(ch)
	except:
		return chr(ch)


LEFT 	= "lc"
RIGHT 	= "rc"
END 	= "ec"
RESET 	= "rs"

# LS_COLORS special file codes.
NORMAL 		= "no"
FILE		= "fi"
DIRECTORY	= "di"
LINK		= "ln"
ORPHAN		= "or"
MISSING		= "mi"
PIPE		= "pi"
SOCKET		= "so"
BLOCKDEV	= "bd"
CHARDEV		= "cd"
DOOR		= "do"
EXEC		= "ex"
SETUID		= "su"
SETGID		= "sg"
STICKY		= "st"
OTHERWRITE	= "ow"
STOTHERWRITE	= "tw"

if __name__ == "__main__":
	import sys
	import os
	lsc = ""
	formcol, special, exten = get_colors()
	try:
		if sys.argv[1] == "test": # generate a test directory with all file extensions
			os.system("mkdir test")
			os.system("touch" + " ".join("test/"+ext for ext in exten.keys()))
			sys.exit()
	except:
		pass

	# Format left/right/exit/reset color codes.
	for compname in formcol.keys():
		comp = formcol[compname]
		if comp != "":
			lsc += compname+"="+comp+":"
	# Format default file/folder colors.
	for compname in special.keys():
		comp = special[compname]
		if comp != "":
			lsc += compname+"="+comp+":"
	# Format extensions.
	for compname in sorted(exten.keys()):
		comp = exten[compname]
		if comp != "":
			if compname.startswith("*"):
				lsc += compname+"="+comp+":"
			elif compname.startswith("-"):
				lsc += compname+"="+comp+":"
			else:
				lsc += "*."+compname.lstrip("*.")+"="+comp+":"
	try:
		sys.stdout.buffer.write(lsc.encode('utf-8'))
	except:
		print(lsc.encode('utf-8')) # python2

