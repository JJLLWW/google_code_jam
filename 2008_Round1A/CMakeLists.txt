project(2008_round1A)
cmake_minimum_required(VERSION 3.11.0)

set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)

set(NAME1 min_scal_prod)
set(NAME2 milkshakes)

add_executable(${NAME1} ${NAME1}.cpp)
add_executable(${NAME2} ${NAME2}.cpp)