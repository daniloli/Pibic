import seaborn as sns


d=input('digite o valor da janela(maior que 0):')
serie=raw_input('digite a serie sobre a qual deseja manipular(open, close, high, low, volume:)')
while (serie != 'open'and serie != 'close'and serie != 'high'and serie != 'low' and serie != 'volume'):
    print 'serie nao definida!'
    serie=raw_input('digite a serie sobre a qual deseja manipular(open, close, high, low, volume:)')
if serie == 'open':
    serie='opn'
serie='serie='+serie
exec serie
Rt=[]
for i in range (d,len(serie)):
    Rt.append(log(serie[i]/serie[i-d]))
squares=list(map(lambda x:pow(x,2),Rt))
soma=[]
for i in range (len(Rt)-d):
    soma.append(sum(squares[i:i+d])/d)
    
    
theil=[]
for i in range(len(serie)-d):
    Mu=sum(serie[i:i+d])/d
    janela=[]
    for j in range(d):
        s=(serie[i+d]/Mu)+log(serie[i+d]/Mu)
        janela.append(s)
    theil.append((sum (janela)/d))

figure(1)
plot(Rt)
xlabel('t')
title('Retorno log d=%d'%d)

savefig('Retornolog d=%d.jpeg'%d)
figure(2)
plot(soma)
xlabel('t')
title('Observacoes em janelas moveis d=%d'%d)
savefig('somajmd=%d.jpeg'%d) 
figure (3)
sns.distplot(Rt,hist=False)
title('Densityplot Rl d=%d'%d)
savefig('dp retornolog d=%d.jpeg'%d)
figure(4)
sns.distplot(soma,hist=False)
title('densityplot jm d=%d'%d)
savefig('dp soma jm d=%d.jpeg'%d)
figure(5)
plot(theil)
title('Indice de Theil, d=%d'%d)
savefig('Indice de Theil, d=%d'%d)
