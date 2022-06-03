cmake_minimum_required(VERSION 3.11.0)
project(2009_QR)

set(CXX_STANDARD 17)
set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(NAME1 alien_language)
set(NAME2 watersheds)

add_executable(${NAME1} ${NAME1}.cpp)
add_executable(${NAME2} ${NAME2}.cpp)