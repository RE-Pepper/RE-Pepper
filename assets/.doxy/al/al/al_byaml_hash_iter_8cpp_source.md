

# File alByamlHashIter.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Yaml**](dir_88abf051c89dccbd64e4b1732f597ee0.md) **>** [**alByamlHashIter.cpp**](al_byaml_hash_iter_8cpp.md)

[Go to the documentation of this file](al_byaml_hash_iter_8cpp.md)


```C++
#include <Yaml/alByamlHashIter.h>

namespace al
{

const ByamlHashPair* ByamlHashIter::findPair( int keyIdx ) const
{
        const ByamlHashPair* table = getPairTable();
        int                  low   = 0;

        if ( mData )
        {
                int high = getSize();
                if ( high > 0 )
                {
                        const ByamlHashPair* pair;
                        int                  idx;
                        while ( true )
                        {
                                idx           = ( low + high ) / 2;
                                pair          = &table[ idx ];
                                const int res = keyIdx - ( pair->getKeyIndex() );
                                if ( res < 0 )
                                        high = idx;
                                if ( res > 0 )
                                        low = idx + 1;
                                if ( res == 0 )
                                        return &table[ idx ];
                                if ( high <= low )
                                        break;
                        }
                }
        }

        return nullptr;
}

} // namespace al
```


