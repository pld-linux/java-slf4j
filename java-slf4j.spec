# TODO:
# - build from source (using maven)
# - tests?
# - split into subpackages?

%define		srcname		slf4j
Summary:	Simple Logging Facade for Java
Summary(pl.UTF-8):	Simple Logging Facade for Java - prosta fasada do logowania dla Javy
Name:		java-%{srcname}
Version:	1.7.30
Release:	1
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:	MIT and ASL 2.0
Group:		Libraries/Java
#Source0Download: https://github.com/qos-ch/slf4j/releases
Source0:	https://github.com/qos-ch/slf4j/archive/v_%{version}/%{srcname}-%{version}.tar.gz
# Source0-md5:	332f34940151b920724f1a0157a19196
Source1:	https://repo1.maven.org/maven2/org/slf4j/jcl-over-slf4j/%{version}/jcl-over-slf4j-%{version}.jar
# Source1-md5:	69ad224b2feb6f86554fe8997b9c3d4b
Source2:	https://repo1.maven.org/maven2/org/slf4j/jul-to-slf4j/%{version}/jul-to-slf4j-%{version}.jar
# Source2-md5:	f2c78cb93d70dc5dea0c50f36ace09c1
Source3:	https://repo1.maven.org/maven2/org/slf4j/log4j-over-slf4j/%{version}/log4j-over-slf4j-%{version}.jar
# Source3-md5:	3b22990e0f731c139873e7c5f48853dd
Source4:	https://repo1.maven.org/maven2/org/slf4j/osgi-over-slf4j/%{version}/osgi-over-slf4j-%{version}.jar
# Source4-md5:	60d20e658d5bfa27db742fd412746fbb
Source5:	https://repo1.maven.org/maven2/org/slf4j/slf4j-android/%{version}/slf4j-android-%{version}.jar
# Source5-md5:	60567058a512183cd953271c03c55360
Source6:	https://repo1.maven.org/maven2/org/slf4j/slf4j-api/%{version}/slf4j-api-%{version}.jar
# Source6-md5:	f8be00da99bc4ab64c79ab1e2be7cb7c
Source7:	https://repo1.maven.org/maven2/org/slf4j/slf4j-ext/%{version}/slf4j-ext-%{version}.jar
# Source7-md5:	e20ffb6713978cc8bd90835e36c5cc66
Source8:	https://repo1.maven.org/maven2/org/slf4j/slf4j-jcl/%{version}/slf4j-jcl-%{version}.jar
# Source8-md5:	046fbb4bb678f459d918067fb8d41efa
Source9:	https://repo1.maven.org/maven2/org/slf4j/slf4j-jdk14/%{version}/slf4j-jdk14-%{version}.jar
# Source9-md5:	84d1846ed0e770858885ee9742a9d620
Source10:	https://repo1.maven.org/maven2/org/slf4j/slf4j-log4j12/%{version}/slf4j-log4j12-%{version}.jar
# Source10-md5:	78f1ff83b38c52a30a278dec6e023a6d
Source11:	https://repo1.maven.org/maven2/org/slf4j/slf4j-migrator/%{version}/slf4j-migrator-%{version}.jar
# Source11-md5:	2b656f312a383a2b53e8c5eb9f86a1b8
Source12:	https://repo1.maven.org/maven2/org/slf4j/slf4j-nop/%{version}/slf4j-nop-%{version}.jar
# Source12-md5:	a693866cc58b82118054b26b698aed3a
Source13:	https://repo1.maven.org/maven2/org/slf4j/slf4j-simple/%{version}/slf4j-simple-%{version}.jar
# Source13-md5:	6577a4799237b81bc9bdc153d6347c30

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
%setup -q -n %{srcname}-v_%{version}

install -d built-jars
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	%{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE13} built-jars

%build
# TODO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}}

# jars
for j in built-jars/*%{version}.jar; do
	n=$(basename $j -%{version}.jar)
	cp -p $j $RPM_BUILD_ROOT%{_javadir}/$n-%{version}.jar
	ln -s $n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$n.jar
done

# FIXME: package real apidocs again (after building with mvn)
#cp -rf site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/slf4j-%{version}
cp -pr slf4j-site/src/site/pages $RPM_BUILD_ROOT%{_javadocdir}/slf4j-%{version}
ln -sf slf4j-%{version} $RPM_BUILD_ROOT%{_javadocdir}/slf4j

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
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
