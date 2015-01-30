# TODO:
# - build from source
# - tests?
# - split into subpackages?

%define		srcname		slf4j
%include	/usr/lib/rpm/macros.java
Summary:	Simple Logging Facade for Java
Summary(pl.UTF-8):	Simple Logging Facade for Java - prosta fasada do logowania dla Javy
Name:		java-%{srcname}
Version:	1.7.10
Release:	1
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:	MIT and ASL 2.0
Group:		Libraries/Java
Source0:	http://www.slf4j.org/dist/%{srcname}-%{version}.tar.gz
# Source0-md5:	dce921c782f761dd30607a4f4d631644
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

%description -l pl.UTF-8
SLF4J (Simple Logging Facade for Java - prosta fasada do logowania dla
Javy) ma służyć jako prosta fasada dla różnych API logujących,
pozwalająca użytkownikowi końcowemu podłączyć pożądaną implementację w
trakcie wdrożenia. SLF4J pozwala także na stopniową migrację ze
szkieletu Jakarta Commons Logging (JCL).

%package javadoc
Summary:	API documentation for SFL4J
Summary(pl.UTF-8):	Dokumentacja API biblioteki SFL4J
Group:		Documentation

%description javadoc
API documentation for SFL4J.

%description javadoc -l pl.UTF-8
Dokumentacja API biblioteki SFL4J.

%prep
%setup -q -n %{srcname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}}

# jars
for j in *%{version}.jar; do
	n=$(basename $j -%{version}.jar)
	cp -p $j $RPM_BUILD_ROOT%{_javadir}/$n-%{version}.jar
	ln -s $n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$n.jar
done

cp -rf site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/slf4j-%{version}
ln -sf slf4j-%{version} $RPM_BUILD_ROOT%{_javadocdir}/slf4j

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md site/changes/*.txt
%{_javadir}/jcl-over-slf4j-%{version}.jar
%{_javadir}/jcl-over-slf4j.jar
%{_javadir}/jul-to-slf4j-%{version}.jar
%{_javadir}/jul-to-slf4j.jar
%{_javadir}/log4j-over-slf4j-%{version}.jar
%{_javadir}/log4j-over-slf4j.jar
%{_javadir}/osgi-over-slf4j-%{version}.jar
%{_javadir}/osgi-over-slf4j.jar
%{_javadir}/slf4j-android-%{version}.jar
%{_javadir}/slf4j-android.jar
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

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/slf4j-%{version}
%{_javadocdir}/slf4j
