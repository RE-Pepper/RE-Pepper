

# File alSequence.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Sequence**](dir_df777ac7bdb81f33f045aae9390ad921.md) **>** [**alSequence.cpp**](al_sequence_8cpp.md)

[Go to the documentation of this file](al_sequence_8cpp.md)


```C++
#include <Scene/alScene.h>
#include <Sequence/alSequence.h>

namespace al
{

void Sequence::init()
{
}

void Sequence::unk1()
{
        if ( mCurrentScene )
                mCurrentScene->drawMainTop();
}

void Sequence::unk2()
{
        if ( mCurrentScene )
                mCurrentScene->drawSubTop();
}

void Sequence::unk3()
{
        if ( mCurrentScene )
                mCurrentScene->drawMainBottom();
}

bool Sequence::isDisposable() const
{
        return true;
}

bool Sequence::unk4()
{
        return false;
}

int Sequence::unk5()
{
        return unk6() ^ 1;
}

} // namespace al
```


