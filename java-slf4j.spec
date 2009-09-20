#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	tests		# don't build and run tests

%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif
#
%include	/usr/lib/rpm/macros.java

%define		srcname		slf4j
Summary:	Simple Logging Facade for Java
Name:		java-slf4j
Version:	1.5.8
Release:	0.1
License:	MIT
Group:		Libraries/Java
Source0:	http://xatka.net/~z/PLD/slf4j-1.5.8.tar.bz2
# Source0-md5:	841e16c3d5d5a323ceabfc6bdce10bb8
Source1:	%{name}-build.xml
URL:		http://www.slf4j.org/
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	javassist
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-logging
BuildRequires:	java-log4j
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Logging Facade for Java or (SLF4J) serves as a simple facade or
abstraction for various logging frameworks, e.g. java.util.logging, log4j and
logback, allowing the end user to plug in the desired logging framework at
deployment time.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%package manual
Summary:	Tutorial for %{name}
Group:		Documentation

%description manual
Manual for %{name}.

%prep
%setup -q -n %{srcname}-%{version}
cp %{SOURCE1} build.xml

%build

export JAVA_HOME="%{java_home}"

# required_jars="jaxp_parser_impl"
# CLASSPATH=$(build-classpath $required_jars)
# export CLASSPATH

export LC_ALL=en_US # source code not US-ASCII

javassist_jar=$(find-jar javassist)
commons_logging_jar=$(find-jar commons-logging-api)
commons_lang_jar=$(find-jar commons-lang)
log4j_jar=$(find-jar log4j)

%ant jars \
  -Djavassist-jar=$javassist_jar \
  -Dcommons-logging-jar=$commons_logging_jar \
  -Dcommons-lang-jar=$commons_lang_jar \
  -Dlog4j-jar=$log4j_jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a dist/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
