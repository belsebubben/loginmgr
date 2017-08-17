Name:		loginmgr
Epoch:		1
Version:	0.1
Release:	1%{?dist}
BuildArch:	noarch
Summary:	loginmgr command line login / password manager
Group:		Applications/Text
# The GPL v2
# https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
License:	GNU GENERAL PUBLIC LICENSE v2
URL:		https://github.com/belsebubben/loginmgr
Source0:	https://github.com/belsebubben/loginmgr/blob/master/loginmgr.py
Source1:	https://github.com/belsebubben/loginmgr/blob/master/README.md

#BuildRequires:    -

Requires:          python3
Requires:          python3-cryptography
Provides:          loginmgr


%description
loginmgr: A simple to use login / password manager for use on the command line.

%prep
#%setup -q
echo "prep"

%build
#make 
echo "Making"

%install
echo "installing"
mkdir %{buildroot}

install -p -D -m 0755 %{SOURCE0} \
    %{buildroot}/loginmgr

%pre
echo "pre"

%post
echo "post"

%preun
echo "preun"

%postun
echo "postun"

%files
%{_bindir}/loginmgr

%changelog
* Thu Aug 13 2016 Carl Hartman <https://github.com/belsebubben> - 0.1
- Inifial build