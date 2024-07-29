import numpy as np
import matplotlib

gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        print("testing", gui)
        matplotlib.use(gui)
        print(gui, "works?")
        from matplotlib import pyplot as plt
        break
    except:
        continue
        
matplotlib.use("Qt5Agg")
print("Using:",matplotlib.get_backend())
import matplotlib.pyplot as plt


plt.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']




g = lambda x: np.log(x + 2) # for e^x = x + 2 fixed point analysis try unstable x0 = -1.8414056696


x0 = 0.2
iterations = 5
xk = [x0]
yk = [g(x0)]
for i in range(iterations):
    xk.append(g(xk[i]))
    yk.append(g(xk[i]))

fig,axes=plt.subplots(figsize=(13.5,4.5),ncols=3)
#fig.tight_layout()

x_cont=np.linspace(-1.99,5,10000)
for ax in axes:
    # function y=g(x)
    ax.plot(x_cont,[g(x) for x in x_cont],ls='-',color='C0')
    ax.plot(x_cont,x_cont,ls='-',color='black')


ax=axes[0]
ax.plot((xk[0]), (xk[0]),ls='', color='crimson',marker='o',markerfacecolor='white')
ax.plot((xk[-1]), (xk[-1]),ls='', color='crimson',marker='o')
ax.annotate('', xy=(xk[0], 0.6*(xk[0]+yk[1])),  xycoords='data',xytext=(xk[0], xk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate('', xy=(0.6*(xk[1]+xk[0]), yk[0]),  xycoords='data',xytext=(xk[0], yk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
for i in range(1):
    xmin=xk[i]
    xmax=xk[i+1]
    ymin=yk[i]
    ymax=yk[i+1]
    if i==0: ymin=xk[0]
    ax.plot((xmin, xmin), (ymin, ymax),ls='-', color='crimson')
    ax.plot((xmin, xmax), (ymax, ymax),ls='-', color='crimson')
    ax.plot((xmax), (ymax),ls='', color='crimson',marker='o')

    
ax.annotate(r'$x_0$', xy=(xk[0], -0.05),  xycoords='data',xytext=(xk[0], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate(r'$x_1$', xy=(xk[1], -0.05),  xycoords='data',xytext=(xk[1], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')

    
ax.annotate(r'$g(x_0)$', xy=(-0.05, yk[1]),  xycoords='data',xytext=(-0.3,yk[1]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')
    
    

ax=axes[1]
ax.plot((xk[0]), (xk[0]),ls='', color='crimson',marker='o',markerfacecolor='white')
ax.plot((xk[-1]), (xk[-1]),ls='', color='crimson',marker='o')
ax.annotate('', xy=(xk[0], 0.6*(xk[0]+yk[1])),  xycoords='data',xytext=(xk[0], xk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate('', xy=(0.6*(xk[1]+xk[0]), yk[0]),  xycoords='data',xytext=(xk[0], yk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate('', xy=(xk[1], yk[1] + 0.7*(-yk[1]+yk[2])),  xycoords='data',xytext=(xk[1], yk[1]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
for i in range(2):
    xmin=xk[i]
    xmax=xk[i+1]
    ymin=yk[i]
    ymax=yk[i+1]
    if i==0: ymin=xk[0]
    ax.plot((xmin, xmin), (ymin, ymax),ls='-', color='crimson')
    ax.plot((xmin, xmax), (ymax, ymax),ls='-', color='crimson')
    ax.plot((xmax), (ymax),ls='', color='crimson',marker='o')

    
ax.annotate(r'$x_0$', xy=(xk[0], -0.05),  xycoords='data',xytext=(xk[0], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate(r'$x_1$', xy=(xk[1], -0.05),  xycoords='data',xytext=(xk[1], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate(r'$x_2$', xy=(xk[2], -0.05),  xycoords='data',xytext=(xk[2], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')

    
ax.annotate(r'$g(x_0)$', xy=(-0.05, yk[1]),  xycoords='data',xytext=(-0.3,yk[1]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')
ax.annotate(r'$g(x_1)$', xy=(-0.05, yk[2]),  xycoords='data',xytext=(-0.3,yk[2]),  
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')
    
    
    
    
ax=axes[2]
ax.plot((xk[0]), (xk[0]),ls='', color='crimson',marker='o',markerfacecolor='white')
ax.plot((xk[-1]), (xk[-1]),ls='', color='crimson',marker='o')
ax.annotate('', xy=(xk[0], 0.6*(xk[0]+yk[1])),  xycoords='data',xytext=(xk[0], xk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate('', xy=(0.6*(xk[1]+xk[0]), yk[0]),  xycoords='data',xytext=(xk[0], yk[0]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate('', xy=(xk[1], yk[1] + 0.7*(-yk[1]+yk[2])),  xycoords='data',xytext=(xk[1], yk[1]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.5",facecolor='crimson',color='crimson'),
            horizontalalignment='center',verticalalignment='top')
for i in range(iterations):
    xmin=xk[i]
    xmax=xk[i+1]
    ymin=yk[i]
    ymax=yk[i+1]
    if i==0: ymin=xk[0]
    ax.plot((xmin, xmin), (ymin, ymax),ls='-', color='crimson')
    ax.plot((xmin, xmax), (ymax, ymax),ls='-', color='crimson')
    ax.plot((xmax), (ymax),ls='', color='crimson',marker='o')

    
ax.annotate(r'$x_0$', xy=(xk[0], -0.05),  xycoords='data',xytext=(xk[0], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate(r'$x_1$', xy=(xk[1], -0.05),  xycoords='data',xytext=(xk[1], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')
ax.annotate(r'$x_2$', xy=(xk[2], -0.05),  xycoords='data',xytext=(xk[2], -0.2), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='top')

    
ax.annotate(r'$g(x_0)$', xy=(-0.05, yk[1]),  xycoords='data',xytext=(-0.3,yk[1]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')
ax.annotate(r'$g(x_1)$', xy=(-0.05, yk[2]),  xycoords='data',xytext=(-0.3,yk[2]),  
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')
ax.annotate(r'$g(x_2)$', xy=(-0.05, yk[3]),  xycoords='data',xytext=(-0.3,yk[3]), 
            textcoords='data',arrowprops=dict(arrowstyle="->, head_width=0.2",facecolor='black',color='black'),
            horizontalalignment='center',verticalalignment='center')



for ax in axes:
    squareside=5
    centerx=2
    centery=2
    ax.set_xlim([centerx-squareside,centerx+squareside])
    ax.set_ylim([centery-squareside,centery+squareside])
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    xroot = 1.14624
    yroot = 1.133 
    ax.set_xlim([xroot-1.5,xroot+1.5])
    ax.set_ylim([yroot-1.5,yroot+1.5])

    ax.text(ax.get_xlim()[1],0.05,r'$x$', fontsize=15)
    ax.text(-0.1,ax.get_ylim()[1],r'$y$', fontsize=15)

    #ax.axhline(y=0,ls='-',color='darkgrey')
    #ax.axvline(x=0,ls='-',color='darkgrey')
    #ax.axis('off')

    ax.text(1.85,2.0,r'$y=x$', fontsize=20, rotation=47, va='center', ha='center')
    ax.text(2.1,1.25,r"$y=g(x)$", fontsize=20, rotation=0, va='center', ha='center')
    
plt.show()
