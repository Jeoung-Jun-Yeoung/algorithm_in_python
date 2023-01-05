#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

char userID[10][32];
char pwdID[10][32];
int stop = 0;
int count = 0;

void parsing_text(int fd, char *location)
{
    for (int i = 0;; i++)
    {
        if (read(fd, &location[i], 1) <= 0)
        {
            stop = 1;
            break;
        }
        if (location[i] == ' ' || location[i] == '\n')
        {
            location[i] = '\0';
            break;
        }
    }
}

void get_user_list()
{
    int fd;
    fd = open("list.txt", O_RDONLY);
    if (fd < 0)
    {
        printf(1, "init already exec file\n");
        exit();
    }
    for (int i = 0; i < 1; i++)
    {
        if (stop)
        {
            break;
        }
        count++;
        parsing_text(fd, userID[i]);
        parsing_text(fd, pwdID[i]);
    }
}

int check_idpw()
{
    char id[32] = {
        0,
    };
    char pw[32] = {
        0,
    };
    printf(1, "Username: ");
    parsing_text(0, id);
    printf(1, "Password: ");
    parsing_text(0, pw);

    for (int i = 0; i < count; i++)
    {
        if (!strcmp(id, userID[i]))
        {
            if (!strcmp(pw, pwdID[i]))
            {
                return 1;
            }
            return 0;
        }
    }
    return 0;
}

int main(int argc, char *argv[])
{
    int pid, wpid;
    get_user_list();

    while (1)
    {
        if (check_idpw())
            for (;;)
            {
                printf(1, "init: starting login\n");
                pid = fork();
                if (pid < 0)
                {
                    printf(1, "init: fork failed\n");
                    exit();
                }
                if (pid == 0)
                {
                    exec("sh", argv);
                    printf(1, "init: exec sh failed\n");
                    exit();
                }
                while ((wpid = wait()) >= 0 && wpid != pid)
                    printf(1, "zombie!\n");
            }
    }
}