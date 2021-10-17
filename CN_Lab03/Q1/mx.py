import dns.resolver

domain = input('Enter the Domain name : ')

for record in dns.resolver.resolve(domain, 'MX'):
    print('MX record : ', (record.to_text()).split(' ', 1)[1])


# A MX record also called mail exchanger record is a resource record in the Domain Name System that specifies a mail
# server responsible for accepting email messages on behalf of a recipient's domain.
