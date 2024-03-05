\+DatabaseType Text
\ver 5.0
\desc Database type for general-purpose text. Uses \name as record marker (compatible with output of TextPrep.cct).
\+mkrset 
\lngDefault Default
\mkrRecord t

\+mkr dt
\nam *
\lng Default
\mkrOverThis name
\-mkr

\+mkr f
\nam Free Translation
\lng chinese
\mkrOverThis ref
\-mkr

\+mkr g
\nam gloss english
\lng Default
\mkrOverThis m
\-mkr

\+mkr id
\nam ID of Text
\lng English
\mkrOverThis name
\-mkr

\+mkr m
\nam morpheme
\lng IPA93
\mkrOverThis t
\-mkr

\+mkr n
\nam gloss national
\lng chinese
\mkrOverThis m
\-mkr

\+mkr name
\nam Name of Text
\lng English
\mkrOverThis t
\-mkr

\+mkr notes
\nam notes
\lng chinese
\mkrOverThis name
\-mkr

\+mkr p
\nam parts of speech
\lng Default
\mkrOverThis m
\-mkr

\+mkr ref
\nam Reference Number
\lng Default
\+fnt 
\Name Times New Roman
\Size 10
\charset 00
\rgbColor 128,128,128
\-fnt
\mkrOverThis name
\-mkr

\+mkr t
\nam Text
\lng Default
\+fnt 
\Name Times New Roman
\Size 14
\charset 00
\rgbColor 0,0,0
\-fnt
\-mkr

\+mkr title
\nam ti
\lng Default
\mkrOverThis t
\-mkr

\-mkrset

\iInterlinCharWd 8
\+filset 

\-filset

\+jmpset 
\-jmpset

\+template 
\-template
\mkrRecord t
\+PrintProperties 
\header File: &f, Date: &d
\footer Page &p
\topmargin 2.54 cm
\leftmargin 0.64 cm
\bottommargin 2.54 cm
\rightmargin 0.64 cm
\recordsspace 10
\-PrintProperties
\+expset 

\+expRTF Rich Text Format
\+rtfPageSetup 
\paperSize letter
\topMargin 1
\bottomMargin 1
\leftMargin 1.25
\rightMargin 1.25
\gutter 0
\headerToEdge 0.5
\footerToEdge 0.5
\columns 1
\columnSpacing 0.5
\-rtfPageSetup
\-expRTF

\+expSF Standard Format
\-expSF

\expDefault Standard Format
\SkipProperties
\-expset
\-DatabaseType
