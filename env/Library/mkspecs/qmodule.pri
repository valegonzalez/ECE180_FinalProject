QT_BUILD_PARTS += libs tools
QT_QCONFIG_PATH = 

host_build {
    QT_CPU_FEATURES.x86_64 =  sse sse2
} else {
    QT_CPU_FEATURES.x86_64 =  sse sse2
}
QT_COORD_TYPE += double
CONFIG += precompile_header pcre system-sqlite release compile_examples sse2 sse3 ssse3 sse4_1 sse4_2 largefile
QMAKE_QT_VERSION_OVERRIDE = 5
EXTRA_LIBS += -LD:/Anaconda2/envs/ece180final/Library/lib
QT_LFLAGS_SQLITE += sqlite3.lib
EXTRA_INCLUDEPATH += D:/Anaconda2/envs/ece180final/Library/include
sql-plugins    += sqlite
styles         += windows fusion windowsxp windowsvista
