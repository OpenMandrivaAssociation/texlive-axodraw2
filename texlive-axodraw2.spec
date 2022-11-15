Name:		texlive-axodraw2
Version:	58155
Release:	1
Summary:	Feynman diagrams in a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/axodraw2
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axodraw2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axodraw2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/axodraw2.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines macros for drawing Feynman graphs in LaTeX
documents. It is an important update of the axodraw package,
but since it is not completely backwards compatible, we have
given the style file a changed name. Many new features have
been added, with new types of line, and much more flexibility
in their properties. In addition, it is now possible to use
axodraw2 with pdfLaTeX, as well as with the LaTeX-dvips method.
However with pdfLaTeX (and also LuaLaTeX and XeLaTeX), an
external program, axohelp, is used to perform the geometrical
calculations needed for the pdf code inserted in the output
file. The processing involves a run of pdfLaTeX, a run of
axohelp, and then another run of pdfLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/latex/axodraw2
%{_texmfdistdir}/texmf-dist/tex/latex/axodraw2
%doc %{_texmfdistdir}/texmf-dist/doc/latex/axodraw2
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/axohelp.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/axohelp.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
