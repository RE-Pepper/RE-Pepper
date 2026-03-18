

# File alSequence.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Sequence**](dir_61cc125e36c527d3ac6cde3bc5659a45.md) **>** [**alSequence.cpp**](al_sequence_8cpp.md)

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


