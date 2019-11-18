srcfile = strcat(codertarget.freedomk64f.internal.getSpPkgRootDir, '\src\mw_sdk_interface.c');

frt = fopen(srcfile,'rt');
X = fread(frt);
fclose(frt);

X = char(X.');
S1 = '{ GPIO_MAKE_PIN(GPIOA_IDX, 0),  MW_NOT_USED},// PTA0, D8';
S2 = '{ GPIO_MAKE_PIN(GPIOC_IDX, 12), MW_NOT_USED},// PTC12, D8';
Y = strrep(X, S1, S2);

fwt = fopen(srcfile,'wt') ;
fwrite(fwt,Y) ;
fclose(fwt) ;

clear;

% Modify hardware.m
srcfile = strcat(codertarget.freedomk64f.internal.getSpPkgRootDir, '\+freedomk64f\Hardware.m');

frt = fopen(srcfile,'rt');
X = fread(frt);
fclose(frt);

X = char(X.');
S1 = 'PTA0';
S2 = 'PTC12';
Y = strrep(X, S1, S2);

fwt = fopen(srcfile,'wt') ;
fwrite(fwt,Y) ;
fclose(fwt) ;

clear;