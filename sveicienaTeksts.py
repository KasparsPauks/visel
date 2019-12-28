# ++++++++++++++++++++++++++++++++++
#
# Author: Kaspars
# 
# Version   Date        Info
#   1.0     2019    Initial version
#
# ++++++++++++++++++++++++++++++++++
# Sasveicināšanās teksts
hello = '''
\tSveiks spēlmani! Sāksim spēlēt!

Spēles mērķis ir uzminēt datora nejauši izvēlētu vārdu,
izmēģinot vairākus iespējamos vārda burtus. Katra burta
atminēšanas reize dators atver vārda vietas, kur ir
atminēts burts, vai ari nepareiza minējuma gadījuma papildina
karātavas ar kārtējo detaļu. Kad zīmējums ir pabeigts, nepareizo
minējumu skaits ir sasniedzis maksimalo pieļaujamo robežu un
spēle ir beigusies. Minēšanas kļūdu iespējamās kļūdīšanās reizes ir
6-as:
- Galva
- Ķermenis
- 2-as rokas
- 2-as kājas
 Lai veicas!
'''
# Atminamo vārdu saraksts
words = ['karātavas', 'tālrunis', 'kristaps', 'valerijs', 'austrums']
alfabet = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'  # lietojamie burti


# def a(v):
#     ind_alf = alfabet.index(v)
#     key = alfabet[ind_alf]