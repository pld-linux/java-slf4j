# TODO:
# - javadocs?
# - tests?
# - split into subpackages?

%include	/usr/lib/rpm/macros.java

%define		srcname		slf4j
Summary:	Simple Logging Facade for Java
Name:		java-slf4j
Version:	1.6.1
Release:	1
License:	MIT
Group:		Libraries/Java
Source0:	http://www.slf4j.org/dist/slf4j-1.6.1.tar.gz
# Source0-md5:	289d4ce9b710269614e97f1ae6a27906
URL:		http://www.slf4j.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Logging Facade for Java or (SLF4J) serves as a simple
facade or abstraction for various logging frameworks, e.g.
java.util.logging, log4j and logback, allowing the end user to plug in
the desired logging framework at deployment time.

%prep
%setup -q -n %{srcname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
for j in *%{version}.jar; do
  n=$(basename $j -%{version}.jar)
  cp -a $j $RPM_BUILD_ROOT%{_javadir}/$n-%{version}.jar
  ln -s $n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$n.jar
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
