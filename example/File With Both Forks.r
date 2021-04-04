/* Resource fork of example/File With Both Forks */
resource 'STR#' (128) {
	{	/* array StringArray: 1 elements */
		/* [1] */
		"Hello World"
	}
};

resource 'DITL' (128) {
	{	/* array DITLarray: 4 elements */
		/* [1] */
		{153, 47, 173, 105},
		Button {
			enabled,
			"Hello"
		},
		/* [2] */
		{153, 127, 173, 185},
		Button {
			enabled,
			"World"
		},
		/* [3] */
		{12, 86, 44, 118},
		Icon {
			disabled,
			128
		},
		/* [4] */
		{50, 18, 143, 197},
		StaticText {
			disabled,
			"WYSIWYG like it's 1990"
		}
	}
};

resource 'ics8' (128) {
	$"0000 0000 00FF FFFF FFFF FF00 0000 0000"
	$"0000 00FF FF00 0000 0000 00FF FF00 0000"
	$"0000 FFFF 0000 0000 0000 0000 FFFF 0000"
	$"00FF FF00 0000 0000 0000 0000 00FF FF00"
	$"00FF 0000 0000 0000 0000 0000 0000 FF00"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"FF00 0000 0000 0000 0000 0000 0000 00FF"
	$"00FF 0000 0000 0000 0000 0000 0000 FF00"
	$"00FF FF00 0000 0000 0000 0000 00FF FF00"
	$"0000 FFFF 0000 0000 0000 0000 FFFF 0000"
	$"0000 00FF FF00 0000 0000 00FF FF00 0000"
	$"0000 0000 00FF FFFF FFFF FF"
};

