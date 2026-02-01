FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc make

RUN useradd -d /home/ctf -m -s /bin/bash ctf

WORKDIR /home/ctf

COPY src/ret2win.c .
RUN gcc -fno-stack-protector -no-pie -o ret2win ret2win.c

RUN echo "LKSPML{r3t_2_w1n_1s_cl4ss1c_h4ck}" > flag.txt

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 flag.txt

EXPOSE 1338

CMD ["socat", "TCP-LISTEN:1338,reuseaddr,fork", "EXEC:./ret2win"]
