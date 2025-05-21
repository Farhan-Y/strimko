from board import strimko
from gui import draw

def main():
    '''
    some random puzzle from the web. to see the reslut of each one you should uncomment the code
    '''    

    ################## UNCOMMENT TO SEE THE ORIINAL AND THE SOLUTION#######################
    # x = strimko(size=4)

    # x.new_link('00','11','22','32')
    # x.new_link('01','10','20','31')
    # x.new_link('02','12','21','30')
    # x.new_link('03','13','23','33')
    # x.add_value(2,2,4)
    # x.add_value(3,1,3)
    # x.add_value(3,3,1)
    
    # print('board before being solved:')
    # print(x)
    # x.solver_csp()
    # print('========\nafter solving: \n ')
    # print(x)
    # assert x.is_solved()
    # draw(x)
    
    ################## UNCOMMENT TO SEE THE ORIINAL AND THE SOLUTION#######################

    # z=strimko(size=5)
    # z.new_link('00','01','02','11','21')
    # z.new_link('10','20','30','40','41')
    # z.new_link('31','33','22','12','03')
    # z.new_link('42','32','23','13','04')
    # z.new_link('43','44','34','24','14')

    # z.add_value(1,0,3)
    # z.add_value(1,1,2)
    # z.add_value(1,3,4)
    # z.add_value(3,2,1)
    # z.add_value(3,3,3)

    # print('board before being solved:')
    # print(z)
    # draw(z)
    # z.solver_csp()
    # print('========\nafter solving: \n ')
    # print(z)
    # assert z.is_solved()
    # draw(z)
    
    #########################################

    b=strimko(size=7)

    b.new_link('00','11','12','03','04','15','25') #app corr
    b.new_link('21','10','01','02','13','24','35') #app corr
    b.new_link('20','30','31','22','32','33','34') #corrected
    b.new_link('60','50','40','41','42','53','44') #app corr
    b.new_link('61','51','52','43','54','55','45') #app corr
    b.new_link('62','63','64','65','66','56','46') #app corr
    b.new_link('23','14','05','06','16','26','36') #app coee


    b.add_value(2,0,7)
    b.add_value(2,2,6)
    b.add_value(4,4,6)
    b.add_value(5,0,5)
    b.add_value(6,0,4)
    b.add_value(4,4,6)
    b.add_value(0,3,1)
    b.add_value(6,3,7)
    b.add_value(0,5,5)
    b.add_value(0,6,3)
    b.add_value(4,6,2)

    print('board before being solved:')
    print(b)
    draw(b)
    b.solver_csp()
    print('========\nafter solving: \n ')
    print(b)
    assert  b.is_solved()
    draw(b)
    
    
    ################## UNCOMMENT TO SEE THE ORIINAL AND THE SOLUTION#######################

    a=strimko(size=9 ,type='soduko')        # when type = soduko adding the links are not neccesary

    a.add_value(0,2,5)

    a.add_value(0,4,6)
    a.add_value(0,6,2)
    a.add_value(0,8,8)

    a.add_value(1,3,7)
    a.add_value(1,7,9)

    a.add_value(2,0,2)
    a.add_value(2,8,7)


    a.add_value(3,0,9)
    a.add_value(3,1,1)
    a.add_value(3,3,6)
    a.add_value(3,7,4)
    a.add_value(4,1,8)
    a.add_value(4,4,1)
    a.add_value(4,7,5)
    a.add_value(5,1,3)
    a.add_value(5,5,7)
    a.add_value(5,7,8)
    a.add_value(5,8,1)



    a.add_value(6,0,3)
    a.add_value(6,8,4)
    a.add_value(7,1,2)
    a.add_value(7,5,6)
    a.add_value(8,0,6)
    a.add_value(8,2,8)
    a.add_value(8,4,4)
    a.add_value(8,6,3)

    print('board before being solved:')
    print(a)
    draw(a)
    a.solver_csp()
    print('========\nafter solving: \n ')
    print(a)
    assert a.is_solved()
    draw(a)
    

if __name__=='__main__':
    main()