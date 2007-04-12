%define product         PlacelessTranslationService
%define version         1.3.4
%define release         1

%define zope_minver     2.7

%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Summary:        PTS is a way of internationalizing (i18n'ing) and localizing (l10n'ing) software for Zope 2
Name:           zope-%{product}
Version:        %{version}
Release:        %mkrel %{release}
License:        GPL
Group:          System/Servers
Source:         http://plone.org/products/pts/releases/%{version}/PlacelessTranslationService-%{version}.tar.bz2
URL:            http://plone.org/products/pts
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       zope >= %{zope_minver}

%description
PTS is a way of internationalizing (i18n'ing) and localizing (l10n'ing)
software for Zope 2.
It's based on the files supported by the GNU gettext set of utilities.

%prep
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(0644, root, root, 0755)
%{software_home}/Products/*



