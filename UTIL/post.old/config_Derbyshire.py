#saveall = True
saveall = False

#var2save = ['ta','hus','u','v','pres']
var2save = ['ta','hus','ua','va','pres','wap','ql','qi','qr','qsn','cl','prw','pr','hfls','hfss','prw','qflux','tnqadv','ppr','tnqvpbl','tnqvc','tnqvlscp','tnqvd','tntadv','tntrlw','tntrsw','tntlscp','tntc','tntpbl','tntd','ts','hur','Q1','Q2','QRad','mueff','I0','SWd','rsdt','rsut','rsus','rsds','rsutcs','rsuscs','rsdscs','rlut','rlutcs','rlds','rldscs','rlus','rluscs','alb_ss','qflux','qfluxPr','qfluxEv','dwater','iQadv','iQnud','iQw','Cd','Ch','Ce','Cdn','Chn','Cen','cltl','cltm','clth','clt','Q11','igs','igs2','sigs','sigs2','omega_up','omega_dn','alpha_up','alpha_dn','rho','mlen','sigs2turb','sigs2conv','igs2turb','igs2conv','Q11min','Q11max','acoef','qlc','qic','qrc','qsnc','tke','lwp','iwp','sigc0','sigc1','alpha_up','w_up','omega_up','alpha_dn','w_dn','omega_dn','cape','T_up','qv_up','omega_ref','w_up_bud','dw_buoy','dw_fric','dw_Kd','dw_entr','dw_transp','buoy','Mf','eps_u','eps_u_org','eps_u_tur','entr_u','detr_u','dTv_up']


lfalaf = '/home/roehrig/Logiciels/LFA/Romain/bin/lfalaf'

tunits = 'seconds since 2000-01-01 0:0:0.0'

# Pour convert2p, niveau en hPa
#levout = [1000.,950.,900.,850.,800.,750.,700,650.,600,550.,500.,450.,400.,350.,300.,250.,200.,150.,100.,50.]
levout = []
for i in range(1,41):
  levout.append(i*25.)
levout.reverse()

# Niveau de print (0, 1 ou 2)
verbose = 2

levoutz = []
for i in range(0,50):
  levoutz.append(10*i)
for i in range(0,201):
  levoutz.append(500+100*i)