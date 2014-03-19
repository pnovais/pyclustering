from dbscan import dbscan;
from support import read_sample;
from support import timedcall;

from samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

def template_clustering(radius, neighb, path, draw = True):
    sample = read_sample(path);
    
    (ticks, clusters) = timedcall(dbscan, sample, radius, neighb, draw);
    print("Sample: ", path, "\t\tExecution time: ", ticks, "\n");
    

def cluster_sample1():
    template_clustering(0.5, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE1);
    
def cluster_sample2():
    template_clustering(1, 2, SIMPLE_SAMPLES.SAMPLE_SIMPLE2);
    
def cluster_sample3():
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE3);
    
def cluster_sample4():
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE4);

def cluster_sample5():
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE5);
 
def cluster_elongate():
    template_clustering(0.5, 3, SIMPLE_SAMPLES.SAMPLE_ELONGATE);
    
def cluster_lsun():
    template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_LSUN);    
    
def cluster_target():
    template_clustering(0.5, 2, FCPS_SAMPLES.SAMPLE_TARGET);    
    
def cluster_two_diamonds():
    "It's hard to choose properly parameters, but it's OK"
    template_clustering(0.15, 7, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS);   
    
def cluster_wing_nut():
    "It's hard to choose properly parameters, but it's OK"
    template_clustering(0.25, 2, FCPS_SAMPLES.SAMPLE_WING_NUT); 
    
def cluster_chainlink():
    template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_CHAINLINK); 
    
def cluster_hepta():
    template_clustering(1, 3, FCPS_SAMPLES.SAMPLE_HEPTA); 
    
def cluster_golf_ball():
    "Toooooooooooo looooong"
    template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_GOLF_BALL); 
    
def cluster_atom():
    template_clustering(15, 3, FCPS_SAMPLES.SAMPLE_ATOM); 

def cluster_tetra():
    template_clustering(0.4, 3, FCPS_SAMPLES.SAMPLE_TETRA);
     
def cluster_engy_time():
    template_clustering(0.4, 3, FCPS_SAMPLES.SAMPLE_ENGY_TIME);

def experiment_execution_time():
    "Performance measurement"
    template_clustering(0.5, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE1, False);
    template_clustering(1, 2, SIMPLE_SAMPLES.SAMPLE_SIMPLE2, False);
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE3, False);
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE4, False);
    template_clustering(0.7, 3, SIMPLE_SAMPLES.SAMPLE_SIMPLE5, False);
    template_clustering(0.5, 3, SIMPLE_SAMPLES.SAMPLE_ELONGATE, False);
    template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_LSUN, False);
    template_clustering(0.5, 2, FCPS_SAMPLES.SAMPLE_TARGET, False);
    template_clustering(0.15, 7, FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS, False);
    template_clustering(0.25, 2, FCPS_SAMPLES.SAMPLE_WING_NUT, False);
    template_clustering(0.5, 3, FCPS_SAMPLES.SAMPLE_CHAINLINK, False);
    template_clustering(1, 3, FCPS_SAMPLES.SAMPLE_HEPTA, False);
    template_clustering(0.4, 3, FCPS_SAMPLES.SAMPLE_TETRA, False);


cluster_sample1();
cluster_sample2();
cluster_sample3();
cluster_sample4();
cluster_sample5();
cluster_elongate();
cluster_lsun();
cluster_target();
cluster_two_diamonds();
cluster_wing_nut();
cluster_chainlink();
cluster_hepta();
cluster_golf_ball();            # it is commented due to long time of processing - it's working absolutely correct!
cluster_atom();
cluster_tetra();
cluster_engy_time();

# experiment_execution_time();