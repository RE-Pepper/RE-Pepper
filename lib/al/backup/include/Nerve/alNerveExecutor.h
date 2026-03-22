#pragma once

#include <Nerve/alNerveKeeper.h>

namespace al
{
class NerveKeeper;

class NerveExecutor : public IUseNerve
{
private:
        al::NerveKeeper* mNerveKeeper;

public:
        void initNerve( const Nerve*, int step = 0 );
        void updateNerve();

public:
        virtual NerveKeeper* getNerveKeeper() const;
        virtual ~NerveExecutor() {};

public:
        NerveExecutor( const char* name );
};

} // namespace al
