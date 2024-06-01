#include <stdint.h>
#include <string>
#include "libMDP.hpp"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size)
{
	std::string inputString(reinterpret_cast<const char*>(Data), Size);
	libMDPParser parser;
	parser.parse(inputString);
	return 0;
}

