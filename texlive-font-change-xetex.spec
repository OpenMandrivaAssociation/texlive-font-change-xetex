Name:		texlive-font-change-xetex
Version:	40404
Release:	2
Summary:	Macros to change text and mathematics fonts in plain XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/font-change-xetex
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change-xetex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change-xetex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of macros that can be used to typeset
"plain" XeTeX documents using any OpenType or TrueType font
installed on the computer system. The macros allow the user to
change the text mode fonts and some math mode fonts. For any
declared font family, various font style, weight, and size
variants like bold, italics, small caps, etc., are available
through standard and custom TeX control statements. Using the
optional argument of the macros, the available XeTeX font
features and OpenType tags can be accessed. Other features of
the package include activating and deactivating hanging
punctuation, and support for special Unicode characters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xetex/font-change-xetex
%doc %{_texmfdistdir}/doc/xetex/font-change-xetex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
