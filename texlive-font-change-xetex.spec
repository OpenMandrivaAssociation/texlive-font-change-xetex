%global tl_name font-change-xetex
%global tl_revision 40404

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2016.1
Release:	%{tl_revision}.1
Summary:	Macros to change text and mathematics fonts in plain XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/plain/font-change-xetex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change-xetex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/font-change-xetex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package consists of macros that can be used to typeset "plain"
XeTeX documents using any OpenType or TrueType font installed on the
computer system. The macros allow the user to change the text mode fonts
and some math mode fonts. For any declared font family, various font
style, weight, and size variants like bold, italics, small caps, etc.,
are available through standard and custom TeX control statements. Using
the optional argument of the macros, the available XeTeX font features
and OpenType tags can be accessed. Other features of the package include
activating and deactivating hanging punctuation, and support for special
Unicode characters.

