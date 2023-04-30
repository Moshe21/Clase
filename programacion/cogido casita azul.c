#include <stdio.h>
#include <string.h>

void menu_ing();
void menu_reg();
void menu_prof();
void menu_estu();
char reg_nom_user[3][20]; // se define una matriz de 3x20 para almacenar los nombres de usuario
char reg_pass_user[3][20]; // se define una matriz de 3x20 para almacenar las contraseñas de usuario
float notas[3][3]; // se define una matriz de 3x3 para almacenar las notas de cada estudiante

int main (){
    int f;
    for(int i = 0; i < 3; i++){ // se pide ingresar los datos de 3 usuarios
        printf("REGISTRO DE USUARIO %d\n", i+1);
        printf("INGRESE EL NOMBRE DE USUARIO: ");
        scanf("%s", reg_nom_user[i]);
        printf("INGRESE LA CONTRASEÑA DE USUARIO: ");
        scanf("%s", reg_pass_user[i]);
    }
    while(f!=3){
        int opcion;
        printf("\nBIENVENIDOS AL COLEGIO CASITA AZUL\n1.INGRESAR\n2.REGISTRARSE\n3.SALIR\nINGRESE UNA OPCIÓN: ");
        scanf("%d", &opcion);
        switch(opcion){
            case 1:{
                    menu_ing();
                    break;
                }
            case 2:{
                    menu_reg();
                    break;
                }
            case 3:{
                    f=3;
                    break;
                }
            default:
                printf("\nERROR: OPCION INVALIDA. INTENTE NUEVAMENTE.\n");
        }
    }
    printf("\nQUE TENGAN UN BUEN DIA, LES DESEA COLEGIO CASITA AZUL.\n");
}

void menu_ing(){
    char nom_user[20];
    char pass_user[20];
    printf("\nINGRESAR:\nUSUARIO: ");
    scanf("%s", nom_user);
    printf("CONTRASEÑA: ");
    scanf("%s", pass_user);
    int i;
    for(i=0; i<3; i++){ // se busca el usuario ingresado en la lista de usuarios registrados
        if(strcmp(reg_nom_user[i], nom_user) == 0 && strcmp(reg_pass_user[i], pass_user) == 0){
            printf("\nBIENVENIDO %s\n", nom_user);
            if(i == 0){ // si el usuario es el profesor, se muestra el menú de profesor
                menu_prof();
            }else{ // si el usuario es un estudiante, se muestra el menú de estudiante
                menu_estu(i);
            }
            break;
        }
    }
    if(i == 3){ // si se llega al final de la lista de usuarios y no se ha encontrado el usuario ingresado
        printf("\nERROR: EL USUARIO NO ESTÁ REGISTRADO.\n");
    }
}

void menu_reg(){
    int i;
    for(i=0; i<3; i++){ // se busca una posición vacía en la lista de usuarios registrados
        if(reg_nom_user[i][0] == '\0'){
            break;
        }
    }
    if(i == 3){ // si no se encuentra una posición vacía
        printf("\nERROR: NO SE PUEDEN REGISTRAR MAS USUARIOS.\n");
        return;
    }
    printf("\nREGISTRARSE:\nUSUARIO
