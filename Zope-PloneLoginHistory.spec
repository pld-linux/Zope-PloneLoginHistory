%define		zope_subname	PloneLoginHistory
Summary:	Plone Login History
Summary(pl):	Historia logowañ dla Plone
Name:		Zope-%{zope_subname}
Version:	0.2.0
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://www.easyleading.org/Downloads/PloneLoginHistory-0.2.0.tar.gz
# Source0-md5:	52bd599d7cd77d408c13fbf6c35e9da8
URL:		http://www.easyleading.org/Products/PloneLoginHistory/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF >= 1:1.4.2
Requires:	Zope-CMFPlone >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plone Login History.

%description -l pl
Historia logowañ dla Plone.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af Extensions i18n skins storages *.py *.gif version.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/%{name}
