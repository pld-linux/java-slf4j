#!/bin/sh

cat << EOF
<project name="slf4j" default="jars" basedir=".">
  <description>
    PLD build file for slf4j
  </description>

  <property name="build" location="build"/>
  <property name="dist"  location="dist"/>
  <property name="tests.reports" location="reports"/>
  <property name="tests.build" location="tests-build"/>
  <property name="source" value="1.5"/>
  <property name="target" value="1.5"/>
  <property name="pname" value="commons-net"/>
  <property name="compiler" value="sun"/>

  <property name="commons-lang-jar" value="/usr/share/java/commons-lang.jar"/>
  <property name="commons-logging-jar" value="/usr/share/java/commons-logging-api.jar"/>
  <property name="javassist-jar" value="/usr/share/java/javassist.jar"/>
  <property name="log4j-jar" value="/usr/share/java/log4j.jar"/>

  <target name="clean" description="clean up" >
    <delete dir="\${build}"/>
    <delete dir="\${dist}"/>
    <!--
      <delete dir="\${tests.reports}"/>
      <delete dir="\${tests.build}"/>
     -->
  </target>

  <target name="init">
    <tstamp/>
    <mkdir dir="\${build}"/>
    <mkdir dir="\${dist}"/>
    <!--
      <mkdir dir="\${tests.reports}"/>
      <mkdir dir="\${tests.build}"/>
     -->
  </target>

  <target name="compile-slf4j-api" depends="init">
    <mkdir dir="\${build}/slf4j-api"/>
    <javac srcdir="slf4j-api/src/main/java"
          destdir="\${build}/slf4j-api"
           source="\${source}"
           target="\${target}" />
  </target>

  <path id="slf4j-api">
    <pathelement location="\${build}/slf4j-api"/>
  </path>

  <target name="compile-slf4j-jdk14" depends="init">
    <mkdir dir="\${build}/slf4j-jdk14"/>
    <javac srcdir="slf4j-jdk14/src/main/java"
          destdir="\${build}/slf4j-jdk14"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile-jcl-over-slf4j" depends="init,compile-slf4j-api,compile-slf4j-jdk14">
    <mkdir dir="\${build}/jcl-over-slf4j"/>
    <javac srcdir="jcl-over-slf4j/src/main/java"
          destdir="\${build}/jcl-over-slf4j"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile-jul-to-slf4j" depends="init">
    <mkdir dir="\${build}/jul-to-slf4j"/>
    <javac srcdir="jul-to-slf4j/src/main/java"
          destdir="\${build}/jul-to-slf4j"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile-log4j-over-slf4j" depends="init">
    <mkdir dir="\${build}/log4j-over-slf4j"/>
    <javac srcdir="log4j-over-slf4j/src/main/java"
          destdir="\${build}/log4j-over-slf4j"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile-slf4j-ext" depends="init">
    <mkdir dir="\${build}/slf4j-ext"/>
    <javac srcdir="slf4j-ext/src/main/java"
          destdir="\${build}/slf4j-ext"
           source="\${source}"
           target="\${target}">
      <classpath>
        <path refid="slf4j-api"/>
        <pathelement location="\${commons-lang-jar}"/>
        <pathelement location="\${javassist-jar}"/>
      </classpath>
    </javac>
  </target>

  <target name="compile-slf4j-jcl" depends="init">
    <mkdir dir="\${build}/slf4j-jcl"/>
    <javac srcdir="slf4j-jcl/src/main/java"
          destdir="\${build}/slf4j-jcl"
           source="\${source}"
           target="\${target}">
      <classpath>
        <path refid="slf4j-api"/>
        <pathelement location="\${commons-logging-jar}"/>
      </classpath>
    </javac>
  </target>

  <target name="compile-slf4j-log4j12" depends="init">
    <mkdir dir="\${build}/slf4j-log4j12"/>
    <javac srcdir="slf4j-log4j12/src/main/java"
          destdir="\${build}/slf4j-log4j12"
           source="\${source}"
           target="\${target}">
      <classpath>
        <path refid="slf4j-api"/>
        <pathelement location="\${log4j-jar}"/>
      </classpath>
    </javac>
  </target>

  <target name="compile-slf4j-migrator" depends="init">
    <mkdir dir="\${build}/slf4j-migrator"/>
    <javac srcdir="slf4j-migrator/src/main/java"
      destdir="\${build}/slf4j-migrator"
      source="\${source}"
      target="\${target}" />
  </target>

  <target name="compile-slf4j-nop" depends="init">
    <mkdir dir="\${build}/slf4j-nop"/>
    <javac srcdir="slf4j-nop/src/main/java"
          destdir="\${build}/slf4j-nop"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile-slf4j-simple" depends="init">
    <mkdir dir="\${build}/slf4j-simple"/>
    <javac srcdir="slf4j-simple/src/main/java"
          destdir="\${build}/slf4j-simple"
           source="\${source}"
           target="\${target}">
      <classpath refid="slf4j-api"/>
    </javac>
  </target>

  <target name="compile" depends="compile-jcl-over-slf4j,compile-jul-to-slf4j,compile-log4j-over-slf4j,compile-slf4j-api,compile-slf4j-ext,compile-slf4j-jcl,compile-slf4j-jdk14,compile-slf4j-log4j12,compile-slf4j-nop,compile-slf4j-simple" description="compile all modules"/>

EOF

jars='jcl-over-slf4j
      jul-to-slf4j
      log4j-over-slf4j
      slf4j-api
      slf4j-ext
      slf4j-jcl
      slf4j-jdk14
      slf4j-log4j12
      slf4j-nop
      slf4j-simple'

for j in $jars; do
  m=""
  if [ -r "$j/src/main/resources/META-INF/MANIFEST.MF" ]; then
    m="manifest='$j/src/main/resources/META-INF/MANIFEST.MF'"
  fi
cat << EOF
  <target name='jar-$j' depends='compile-$j'>
    <jar $m
       jarfile='\${dist}/$j.jar'
       basedir='\${build}/$j'/>
  </target>

EOF
done

cat << EOF
  <target name='jars' depends="jar-jcl-over-slf4j,jar-jul-to-slf4j,jar-log4j-over-slf4j,jar-slf4j-api,jar-slf4j-ext,jar-slf4j-jcl,jar-slf4j-jdk14,jar-slf4j-log4j12,jar-slf4j-nop,jar-slf4j-simple" description="build all jars"/>

</project>
EOF
