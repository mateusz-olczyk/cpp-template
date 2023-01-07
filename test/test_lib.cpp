#include <gtest/gtest.h>

#include "lib.hpp"

using namespace myproject;

TEST(Lib, getHelloWorldString) {
    EXPECT_EQ(getHelloWorldString(), "Hello world!");
}
