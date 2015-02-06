%define pkgname sansus-webissimo

Summary:	Sansus Webissimo serif font family
Name:		fonts-ttf-sansus-webissimo
Version:	20110518
Release:	2
License:	Creative Commons Attribution
Group:		System/Fonts/True type
URL:		http://openfontlibrary.org/font/sansus-webissimo
Source0:	%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
"Sansus" - experiment with a new font brought into life in our professional
type foundry. We worked on every single shape and curve to enrich "Sansus"
with elegance and exactitude, try it on phone directories, on your site -
anywhere.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/sansus-webissimo

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/sansus-webissimo
ttmkfdir %{buildroot}%{_xfontdir}/TTF/sansus-webissimo -o %{buildroot}%{_xfontdir}/TTF/sansus-webissimo/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/sansus-webissimo/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/sansus-webissimo \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-sansus-webissimo:pri=50

%__install -d %{buildroot}%{_docdir}/%{name}
cat > %{buildroot}%{_docdir}/%{name}/README << EOF
Family		Sansus Webissimo
Designer	Sergiy S. Tkachenko 
License		CC-BY
Category	Serif

Description

"Sansus" - experiment with a new font brought into life in our professional
type foundry. We worked on every single shape and curve to enrich "Sansus"
with elegance and exactitude, try it on phone directories, on your site -
anywhere.

Full Language Support

Basic Cyrillic, Basic Latin, Euro, Western European
EOF

%files
%doc %{_docdir}/%{name}/README
%dir %{_xfontdir}/TTF/sansus-webissimo
%{_xfontdir}/TTF/sansus-webissimo/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/sansus-webissimo/fonts.dir
%{_xfontdir}/TTF/sansus-webissimo/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-sansus-webissimo:pri=50


%changelog
* Wed Dec 14 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110518-1
+ Revision: 741143
- imported package fonts-ttf-sansus-webissimo

