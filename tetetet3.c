// login: login program in init

#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

char *sh_argv[] = {"sh", 0};
char userID[16][32];
char pwdID[16][32];
char userbuf[32];
char pwdbuf[32];

void get_user_list()
{
    int fd;
    int i, j;
    int cc;
    int flag;
    char c;

    fd = open("list.txt", O_RDONLY);

    for (i = 0; i < 10; i++)
    {
        flag = 0;

        for (j = 0; j < 20; j++)
        {
            cc = read(fd, &c, 1);

            if (cc < 1)
            {
                flag = 1;
                break;
            }

            if (c == ' ')
                break;
            else if (c == '\n')
            {
                flag = 1;
                break;
            }

            userID[i][j] = c;
        }

        if (flag && strlen(userID[i]))
        {
            printf(2, "in login: list.txt error\n");
            break;
        }

        for (j = 0; j < 20; j++)
        {
            cc = read(fd, &c, 1);

            if (cc < 1)
            {
                flag = 1;
                break;
            }
            if (c == '\n')
                break;

            pwdID[i][j] = c;
        }

        if (flag)
            break;
    }

    close(fd);

    //   for (i = 0; i < 10; i++) {
    //      printf(1, "%s %s\n", userID[i], pwdID[i]);
    //   }
}

int check_idpw()
{
    int i;

    for (i = 0; i < 10; i++)
    {
        if (strcmp(userID[i], userbuf) == 0 && strcmp(pwdID[i], pwdbuf) == 0)
        {
            return 0;
        }
    }

    return 1;
}

int main(int argc, char *argv[])
{
    int check = 0;
    int pid, wpid;

    while (1)
    {
        printf(1, "Username: ");
        gets(userbuf, 20);
        userbuf[strlen(userbuf) - 1] = 0;

        printf(1, "Password: ");
        gets(pwdbuf, 20);
        pwdbuf[strlen(pwdbuf) - 1] = 0;

        get_user_list();

        check = check_idpw();

        if (check)
            continue;
        else
        {
            pid = fork();

            if (pid < 0)
            {
                printf(1, "ssu_login: fork failed\n");
                exit();
            }
            if (pid == 0)
            {
                exec("sh", sh_argv);
                printf(1, "ssu_login: sh failed\n");
                exit();
            }
            while ((wpid = wait()) > 0 && wpid != pid)
            {
                printf(1, "zombie!\n");
            }
        }

        break;
    }

    return 0;
}