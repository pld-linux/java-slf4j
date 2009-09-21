# TODO:
# - javadocs?
# - tests?
# - split into subpackages?

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
Source0:	http://xatka.net/~z/PLD/slf4j-%{version}.tar.bz2
# Source0-md5:	841e16c3d5d5a323ceabfc6bdce10bb8
Source1:	%{name}-genbuildxml.sh
URL:		http://www.slf4j.org/
BuildRequires:	java-commons-lang
BuildRequires:	java-commons-logging
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
BuildRequires:	java-log4j
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	javassist
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
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

find -name MANIFEST.MF | xargs sed -i 's,${project.version},%{version},g'

# break build if any macro is left
find -name MANIFEST.MF | ! xargs grep '\${'

%build

export JAVA_HOME="%{java_home}"

export LC_ALL=en_US # source code not US-ASCII

sh %{SOURCE1} > build.xml

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
for j in dist/*.jar; do
  n=$(basename $j .jar)
  cp -a $j $RPM_BUILD_ROOT%{_javadir}/$n-%{version}.jar
  ln -s $n-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$n.jar
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
