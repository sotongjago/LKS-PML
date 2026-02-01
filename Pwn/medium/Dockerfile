FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc make

RUN useradd -d /home/ctf -m -s /bin/bash ctf

WORKDIR /home/ctf

COPY src/rop_gently.c .
# Static compilation for easier ROP
RUN gcc -fno-stack-protector -no-pie -static -o rop_gently rop_gently.c

RUN echo "LKSPML{r0p_ch41n_m4st3r_1n_th3_m4k1ng}" > flag.txt

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 flag.txt

EXPOSE 1339

CMD ["socat", "TCP-LISTEN:1339,reuseaddr,fork", "EXEC:./rop_gently"]
