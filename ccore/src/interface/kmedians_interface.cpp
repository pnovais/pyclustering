/**
*
* Copyright (C) 2014-2018    Andrei Novikov (pyclustering@yandex.ru)
*
* GNU_PUBLIC_LICENSE
*   pyclustering is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   pyclustering is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
*/

#include "interface/kmedians_interface.h"

#include "cluster/kmedians.hpp"


pyclustering_package * kmedians_algorithm(const pyclustering_package * const p_sample, 
                                          const pyclustering_package * const p_initial_medians, 
                                          const double p_tolerance, 
                                          const void * const p_metric)
{
    dataset data, medians;

    p_sample->extract(data);
    p_initial_medians->extract(medians);

    distance_metric<point> * metric = ((distance_metric<point> *) p_metric);
    distance_metric<point> default_metric = distance_metric_factory<point>::euclidean_square();

    if (!metric)
        metric = &default_metric;

    ccore::clst::kmedians algorithm(medians, p_tolerance, *metric);

    ccore::clst::kmedians_data output_result;
    algorithm.process(data, output_result);

    pyclustering_package * package = create_package_container(KMEDIANS_PACKAGE_SIZE);
    ((pyclustering_package **) package->data)[KMEDIANS_PACKAGE_INDEX_CLUSTERS] = create_package(&output_result.clusters());
    ((pyclustering_package **) package->data)[KMEDIANS_PACKAGE_INDEX_MEDIANS] = create_package(&output_result.medians());

    return package;
}
