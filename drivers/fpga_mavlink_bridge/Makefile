# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=g++

# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
LCMDIR=../../LCM/
LCMLIB=../../LCM/lib/libtypes.a

MAVLCMLIB=../../../Fixie/build/lib/liblcmtypes_mav-lcmtypes.a

MAVLIB=/home/$$USER/mav/mavconn/build/lib

CFLAGS=-c -Wall -O3 `pkg-config --cflags lcm bot2-core bot2-param-client` -I/$(LCMDIR) -I../../mavlink-generated -I../../../Fixie/build/include/lcmtypes -I../../../mav/mavlink/build/include/v1.0/ -I../../../mav/mavconn/src/

LIBS=`pkg-config --libs lcm bot2-core bot2-param-client` $(LCMLIB) $(MAVLCMLIB) $(MAVLIB)/libmavconn_lcm.so -Wl,-rpath -Wl,$(MAVLIB)




all: fpga-mavlink-bridge

fpga-mavlink-bridge: fpga-mavlink-bridge.o
	$(CC) fpga-mavlink-bridge.o -o fpga-mavlink-bridge $(LIBS)

fpga-mavlink-bridge.o: fpga-mavlink-bridge.cpp
	$(CC) $(CFLAGS) fpga-mavlink-bridge.cpp

clean:
	rm -rf *o fpga-mavlink-bridge



