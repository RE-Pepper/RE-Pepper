#pragma once

#include <AreaObj/alAreaObj.h>
#include <Factory/alFactory.h>

namespace al
{

typedef CreateFuncPtr<AreaObj>::Type        CreateAreaObjFuncPtr;
typedef NameToCreator<CreateAreaObjFuncPtr> NameToAreaObjCreator;

} // namespace al
