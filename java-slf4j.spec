# TODO:
# - javadocs?
# - tests?
# - split into subpackages?

%define		srcname		slf4j
%include	/usr/lib/rpm/macros.java
Summary:	Simple Logging Facade for Java
Name:		java-%{srcname}
Version:	1.7.5
Release:	1
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:	MIT and ASL 2.0
Group:		Libraries/Java
Source0:	http://www.slf4j.org/dist/%{srcname}-%{version}.tar.gz
# Source0-md5:	0f9ff51370f54308f3fd52338363de25
URL:		http://www.slf4j.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve as
a simple facade for various logging APIs allowing to the end-user to
plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from Jakarta Commons Logging
(JCL).

Logging API implementations can either choose to implement the SLF4J
interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively, it is
possible (and rather easy) to write SLF4J adapters for the given API
implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package javadoc
Summary:	API documentation for %{name}
Group:		Documentation

%description javadoc
This package provides %{summary}.

%package manual
Summary:	Manual for %{name}
Group:		Documentation

%description manual
This package provides documentation for %{name}.

%prep
%setup -q -n %{srcname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
for j in *%{version}.jar; do
	n=$(basename $j -%{version}.jar)
	cp -p $j $RPM_BUILD_ROOT%{_javadir}/$n-%{version}.jar
	ln -s $n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$n.jar
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/jcl-over-slf4j-%{version}.jar
%{_javadir}/jcl-over-slf4j.jar
%{_javadir}/jul-to-slf4j-%{version}.jar
%{_javadir}/jul-to-slf4j.jar
%{_javadir}/log4j-over-slf4j-%{version}.jar
%{_javadir}/log4j-over-slf4j.jar
%{_javadir}/slf4j-api-%{version}.jar
%{_javadir}/slf4j-api.jar
%{_javadir}/slf4j-ext-%{version}.jar
%{_javadir}/slf4j-ext.jar
%{_javadir}/slf4j-jcl-%{version}.jar
%{_javadir}/slf4j-jcl.jar
%{_javadir}/slf4j-jdk14-%{version}.jar
%{_javadir}/slf4j-jdk14.jar
%{_javadir}/slf4j-log4j12-%{version}.jar
%{_javadir}/slf4j-log4j12.jar
%{_javadir}/slf4j-migrator-%{version}.jar
%{_javadir}/slf4j-migrator.jar
%{_javadir}/slf4j-nop-%{version}.jar
%{_javadir}/slf4j-nop.jar
%{_javadir}/slf4j-simple-%{version}.jar
%{_javadir}/slf4j-simple.jar
