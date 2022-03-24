all: dual-tftcp

CFLAGS=-Ofast -fomit-frame-pointer \
 -I/opt/vc/include \
 -I/opt/vc/include/interface/vcos/pthreads \
 -I/opt/vc/include/interface/vmcs_host \
 -I/opt/vc/include/interface/vmcs_host/linux \
 -L/opt/vc/lib
LIBS=-lm -lbcm_host

dual-tftcp: dual-tftcp.c
	cc $(CFLAGS) dual-tftcp.c $(LIBS) -o dual-tftcp
	strip dual-tftcp

clean:
	rm -f dual-tftcp
