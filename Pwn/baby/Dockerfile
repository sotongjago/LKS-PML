FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat gcc make

RUN useradd -d /home/ctf -m -s /bin/bash ctf

WORKDIR /home/ctf

COPY hello_overflow /home/ctf/hello_overflow

RUN echo "LKSPML{b4by_stvck_0v3rfl0w_3z}" > flag.txt

RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 flag.txt

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:./hello_overflow"]
