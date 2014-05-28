# Gandi-dyndns

This little python script allows you to update your gandi.net zonefile. 
This is especially useful if you have a dynamically changing IP address.

## License

This program is licensed under the GNU General Public License v3. See LICENSE for details.

## Usage
```

usage: Gandi-Dyndns [-h] [-ipv4] [-ipv6] [-extipv4 EXTIPV4] [-extipv6 EXTIPV6]
                    [-v]
                    api domain records [records ...]

Update your Gandi.net DNS Zone file

positional arguments:
  api               Your Gandi.Net API Key
  domain            The domain you want to update
  records           The records you want to update

optional arguments:
  -h, --help        show this help message and exit
  -ipv4             Enable IPv4 support
  -ipv6             Enable IPv6 support
  -extipv4 EXTIPV4  Force external IPv4. This can be used to update a record
                    with an IP different than the IP of the server/workstation
                    from which the script is executed
  -extipv6 EXTIPV6  Force external IPv6. This can be used to update a record
                    with an IP different than the IP of the server/workstation
                    from which the script is executed
  -v                Print gandi-dyndns version

```

Example usage:
```
./gandi 12345678987654321 mydomain.eu @ www mail
```



### Thank you
Thanks go to the github user [lembregtse](https://github.com/lembregtse/gandi-dyndns) from which this project orgiginally forked.
