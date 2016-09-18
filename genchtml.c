#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>



#define chtml "c.html"

int main()
{   
    
    FILE* fp;
    time_t rawtime;
    struct tm * timeinfo;
 while(1)
 {
   time (&rawtime);
   timeinfo = localtime (&rawtime);
   char* a = asctime(timeinfo);

   fp = fopen(chtml, "w");

    fprintf(fp,"%s %s %s", "<!DOCTYPE html>    <html>    <head>    </head>    <body>    <h2> C generated page from code </h2>    <a href=\"/index.html\">Back home</a><p>", a," </p>   </body>    </html>");
    fclose(fp);
    sleep(600);
};
    return EXIT_SUCCESS;
}
