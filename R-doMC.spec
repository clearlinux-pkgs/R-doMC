#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-doMC
Version  : 1.3.8
Release  : 49
URL      : https://cran.r-project.org/src/contrib/doMC_1.3.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doMC_1.3.8.tar.gz
Summary  : Foreach Parallel Adaptor for 'parallel'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-foreach
Requires: R-iterators
BuildRequires : R-RUnit
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : buildreq-R

%description
the multicore functionality of the parallel package.

%prep
%setup -q -c -n doMC
cd %{_builddir}/doMC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644184150

%install
export SOURCE_DATE_EPOCH=1644184150
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doMC
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc doMC || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doMC/DESCRIPTION
/usr/lib64/R/library/doMC/INDEX
/usr/lib64/R/library/doMC/Meta/Rd.rds
/usr/lib64/R/library/doMC/Meta/demo.rds
/usr/lib64/R/library/doMC/Meta/features.rds
/usr/lib64/R/library/doMC/Meta/hsearch.rds
/usr/lib64/R/library/doMC/Meta/links.rds
/usr/lib64/R/library/doMC/Meta/nsInfo.rds
/usr/lib64/R/library/doMC/Meta/package.rds
/usr/lib64/R/library/doMC/Meta/vignette.rds
/usr/lib64/R/library/doMC/NAMESPACE
/usr/lib64/R/library/doMC/NEWS
/usr/lib64/R/library/doMC/R/doMC
/usr/lib64/R/library/doMC/R/doMC.rdb
/usr/lib64/R/library/doMC/R/doMC.rdx
/usr/lib64/R/library/doMC/demo/sincMC.R
/usr/lib64/R/library/doMC/doc/gettingstartedMC.R
/usr/lib64/R/library/doMC/doc/gettingstartedMC.Rnw
/usr/lib64/R/library/doMC/doc/gettingstartedMC.pdf
/usr/lib64/R/library/doMC/doc/index.html
/usr/lib64/R/library/doMC/examples/bootMC.R
/usr/lib64/R/library/doMC/help/AnIndex
/usr/lib64/R/library/doMC/help/aliases.rds
/usr/lib64/R/library/doMC/help/doMC.rdb
/usr/lib64/R/library/doMC/help/doMC.rdx
/usr/lib64/R/library/doMC/help/paths.rds
/usr/lib64/R/library/doMC/html/00Index.html
/usr/lib64/R/library/doMC/html/R.css
/usr/lib64/R/library/doMC/tests/doRUnit.R
/usr/lib64/R/library/doMC/unitTests/options.R
/usr/lib64/R/library/doMC/unitTests/runTestSuite.sh
